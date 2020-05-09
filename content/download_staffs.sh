URL=https://github.com/TachibanaYoshino/AnimeGAN/releases/download/Haoyao-style_V1.0/Haoyao-style.zip
ZIP_FILE=./checkpoint/Haoyao-style.zip
TARGET_DIR=./checkpoint/saved_model

mkdir -p ./checkpoint
wget -N $URL -O $ZIP_FILE
mkdir -p $TARGET_DIR
unzip $ZIP_FILE -d $TARGET_DIR
rm $ZIP_FILE

DatesetURL=https://github.com/TachibanaYoshino/AnimeGAN/releases/download/dataset-1/dataset.zip
ZIP_FILE=./dataset.zip
TARGET_DIR=./dataset

rm -rf dataset
wget -N $DatesetURL -O $ZIP_FILE
unzip $ZIP_FILE -d $TARGET_DIR
rm $ZIP_FILE

VGG_FILE=./vgg19_weight/vgg19.npy
wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1U5HCRpZWAbDVLipNoF8t0ZHpwCRX7kdF' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1U5HCRpZWAbDVLipNoF8t0ZHpwCRX7kdF" -O $VGG_FILE && rm -rf /tmp/cookies.txt
