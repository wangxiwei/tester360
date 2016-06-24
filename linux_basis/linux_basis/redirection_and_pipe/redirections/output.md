# 输出重定向

输出重定向有两种符号: ``>``和``>>``

* ``n>``: 将输出从文件描述符 n 重定向到文件。您必须具有该文件的写权限。如果该文件不存在，将创建它。如果该文件已经存在，通常将覆盖所有现有内容，并且没有任何警告。
* ``n>>``: 和上面唯一的不同在于, 如果目标文件存在, 则追加重定向内容到文件尾部, 而不是覆盖原文件。
* ``n>&-``: Close output file descriptor ``n``.

**NOTE**: 文件描述符``n``和重定向符号``>``|``>>``之间不能有空格, 若省略，则默认``1``。

```bash
$ ls > file_list.txt
$ find --help > find_help.txt
$ cat /etc/passwd >> passwd
$ ls x* z* >stdout.txt 2>stderr.txt
```
