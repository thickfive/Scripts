// 删除 tag
git tag -d detached-tag-20241017
// 推送到远端
git push origin :refs/tags/detached-tag-20241017
// 推送所有标签
git push --tag
// 推送所有分支(和标签?)
git push --all

// 推送所有分支(和标签?)
git push --mirror

// 事实表明, git push --all 推送不了游离的分支标签
```
 vvii@macbookpro  ~/Desktop/OpenSource/Scripts  ↱ master  git push --all                                                                                             
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 375 bytes | 375.00 KiB/s, done.
Total 4 (delta 3), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
remote: 
remote: GitHub found 5 vulnerabilities on thickfive/Scripts's default branch (2 high, 3 moderate). To find out more, visit:
remote:      https://github.com/thickfive/Scripts/security/dependabot
remote: 
To https://github.com/thickfive/Scripts.git
   eba1e22..694a975  master -> master
 vvii@macbookpro  ~/Desktop/OpenSource/Scripts   master  git push --all
Everything up-to-date
 vvii@macbookpro  ~/Desktop/OpenSource/Scripts   master  git push --tags                                                                                            
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 8 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 399 bytes | 399.00 KiB/s, done.
Total 4 (delta 3), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
To https://github.com/thickfive/Scripts.git
 * [new tag]         detached-tag-20241017-002 -> detached-tag-20241017-002
```