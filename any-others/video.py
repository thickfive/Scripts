import argparse
import cv2
import os
import re
import shutil

fg_video_path = '/content/AnimeGAN/video/input_video.mp4'
EXTRACT_FREQUENCY = 1

def extract(video_path, image_path, index=EXTRACT_FREQUENCY):
    try:
        shutil.rmtree(image_path)
    except OSError:
        pass
    os.mkdir(image_path)
    video = cv2.VideoCapture()
    if not video.open(video_path):
        print("can not open the video")
        exit(1)
    count = 1
    while True:
        _, frame = video.read()
        if frame is None:
            break
        if count % EXTRACT_FREQUENCY == 0:
            save_path = "{}/{:>04d}.jpg".format(image_path, index)
            cv2.imwrite(save_path, frame)
            index += 1
        count += 1
    video.release()
    print("Totally save {:d} pics".format(index - 1))

def is_frame(path):
    res = re.match(r'\d{4}\.jpg$', path)
    return True if res != None else False

def filter_frame(array):
    res = []
    for item in filter(is_frame, array):
        res.append(item)
    res.sort(reverse=False)
    return res

def combine(image_path, output_path):
    cap = cv2.VideoCapture(fg_video_path)
    fgs = int(cap.get(cv2.CAP_PROP_FPS)) 
    fgs = fgs if fgs > 0 else 25
    pictrue_in_filelist = filter_frame(os.listdir(image_path))
    print(pictrue_in_filelist)
    name = image_path + "/" + pictrue_in_filelist[0]
    img = cv2.imread(name)
    h, w, c = img.shape
    size = (w, h)
    print(f'size: {size}, fgs: {fgs}')

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out_video = output_path + '.mp4'
    video_writer = cv2.VideoWriter(out_video, fourcc, fgs, size)

    for i in range(len(pictrue_in_filelist)):
        pictrue_in_filename = image_path + "/" + pictrue_in_filelist[i]
        img12 = cv2.imread(pictrue_in_filename)
        video_writer.write(img12)
    video_writer.release()
    #print("删除合成的图片数据集")
    #shutil.rmtree(fg_in_bg)
    return out_video

def parse_args():
    desc = "video util"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--type', type=str, default='extract', help='specify which action to take')
    parser.add_argument('--video_path', type=str, default='/content/AnimeGAN/video/input_video.mp4', help='input video path')
    parser.add_argument('--image_path', type=str, default='/content/AnimeGAN/video/input_video', help='output images path')
    parser.add_argument('--output_path', type=str, default='/content/AnimeGAN/video/output_video.mp4', help='output video path')
    """checking arguments"""
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    if args.type == 'extract':
        extract(args.video_path, args.image_path)
        print(f'extract video {args.video_path} into images {args.image_path}')
    elif args.type == 'combine':
        combine(args.image_path, args.output_path)
        print(f'combine images from {args.image_path} into {args.output_path}')
    else:
        print(f'Error: you must specify the argument of type, extract or combine')