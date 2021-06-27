# sql 語法
## CREATE DATABASE - 创建新数据库
## ALTER DATABASE - 修改数据库
## CREATE TABLE - 创建新表
## ALTER TABLE - 变更（改变）数据库表
## DROP TABLE - 删除表
## CREATE INDEX - 创建索引（搜索键）
## DROP INDEX - 删除索引

distinct(0, 1)
0 1
---
a b



ip device
0   A
0   A
1   A
2   A

1   B

2   C


-> group by device
device ip
A      0,0,1,2 -> 0,1,2 -> 3
B      1       -> 1     -> 1
C      2       -> 2     -> 1


-> group by ip
ip device
0   A,A
1   B,A
2   C,A

-> distinct(device)
ip distinct(device)
0   A
1   B,A
2   C,A

-> count(distinct(device))
ip count(distinct(device))
0   2
1   2
2   2
