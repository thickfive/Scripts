// 删除 tag
git tag -d detached-tag-20241017
// 推送到远端
git push origin :refs/tags/detached-tag-20241017
// 推送所有标签
git push --tag
// 推送所有分支
git push --all
// 推送所有分支和标签(包括游离分支上的标签)
git push --mirror