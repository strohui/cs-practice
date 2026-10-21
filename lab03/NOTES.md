git diff:

Позволяет сравнить изменения внутри файла, содержит данные аналогичные для git show

git show:

Показывает коммит, его название, дату, автора, индекс коммита, состояние файла(в случае с calc.py сам код внутри файла), и помечает измененные данные

git log:

Показывает все изменения репозитория, т.н. "логи", а именно: состояние файла на момент последнего коммита, его (коммита) индекс, его путь и его название.





результат работы blame и log -S:

commit eba375bb700b4db749be7d3dc428a2064d57eae6

Author: strohui <timurkucharovich@gmail.com>

Date:   Wed Oct 21 18:36:14 2026 +0300



&#x20;   Добавлено вычитание



diff --git a/lab03/calc.py b/lab03/calc.py

index d3f7fb2..ce74de1 100644

\--- a/lab03/calc.py

+++ b/lab03/calc.py

@@ -2,10 +2,11 @@ c = input('Введите операцию:')

&#x20;a = float(input('Введите число:'))

&#x20;b = float(input('Введите число:'))



\-if c == '+' or c == '-' or c == '\*':

+if c == '+' or c == '-' or c == '\*' or c == '-':

&#x20;    if c == '+':

&#x20;        print(a + b)

\-

\+    elif c == '-' or с == '-':

\+        print(a - b)







PS C:\\Users\\NB\\Documents\\cs-practice\\lab03> git log -S"def" --oneline --lab03/calc.py

fatal: unrecognized argument: --lab03/calc.py

PS C:\\Users\\NB\\Documents\\cs-practice\\lab03> git log -S"def" --oneline --calc.py

fatal: unrecognized argument: --calc.py

PS C:\\Users\\NB\\Documents\\cs-practice\\lab03> git log -S"def" --oneline -- calc.py

PS C:\\Users\\NB\\Documents\\cs-practice\\lab03> git blame calc.py

12fca69 (strohui           2026-10-21 18:35:09 +0300  1) c = input('Введите операцию:')

12fca69 (strohui           2026-10-21 18:35:09 +0300  2) a = float(input('Введите число:'))

12fca69 (strohui           2026-10-21 18:35:09 +0300  3) b = float(input('Введите число:'))

12fca69 (strohui           2026-10-21 18:35:09 +0300  4)

eba375b (strohui           2026-10-21 18:36:14 +0300  5) if c == '+' or c == '-' or c == '\*' or c == '-':

12fca69 (strohui           2026-10-21 18:35:09 +0300  6)     if c == '+':

12fca69 (strohui           2026-10-21 18:35:09 +0300  7)         print(a + b)

0000000 (Not Committed Yet 2026-10-21 18:42:32 +0300  8)     elif c == '-' or c == '-':

eba375b (strohui           2026-10-21 18:36:14 +0300  9)         print(a - b)

c80ed97 (strohui           2026-10-21 18:36:48 +0300 10)     else:

c80ed97 (strohui           2026-10-21 18:36:48 +0300 11)         print(a\*b)

12fca69 (strohui           2026-10-21 18:35:09 +0300 12)

12fca69 (strohui           2026-10-21 18:35:09 +0300 13)

12fca69 (strohui           2026-10-21 18:35:09 +0300 14)

69a090d (strohui           2026-10-20 13:16:27 +0300 15) else:

69a090d (strohui           2026-10-20 13:16:27 +0300 16)     print('Введена неверная операция')

PS C:\\Users\\NB\\Documents\\cs-practice\\lab03> git diff HEAD\~2 HEAD -- calc.py

diff --git a/lab03/calc.py b/lab03/calc.py

index d3f7fb2..97b4b4c 100644

\--- a/lab03/calc.py

+++ b/lab03/calc.py

@@ -2,10 +2,13 @@ c = input('Введите операцию:')

&#x20;a = float(input('Введите число:'))

&#x20;b = float(input('Введите число:'))



\-if c == '+' or c == '-' or c == '\*':

+if c == '+' or c == '-' or c == '\*' or c == '-':

&#x20;    if c == '+':

&#x20;        print(a + b)

\-

\+    elif c == '-' or с == '-':

\+        print(a - b)

\+    else:

\+        print(a\*b)







PS C:\\Users\\NB\\Documents\\cs-practice\\lab03> git log -S"def" --oneline -- calc.py

PS C:\\Users\\NB\\Documents\\cs-practice\\lab03> git blame calc.py

12fca69 (strohui           2026-10-21 18:35:09 +0300  1) c = input('Введите операцию:')

12fca69 (strohui           2026-10-21 18:35:09 +0300  2) a = float(input('Введите число:'))

12fca69 (strohui           2026-10-21 18:35:09 +0300  3) b = float(input('Введите число:'))

12fca69 (strohui           2026-10-21 18:35:09 +0300  4)

eba375b (strohui           2026-10-21 18:36:14 +0300  5) if c == '+' or c == '-' or c == '\*' or c == '-':

12fca69 (strohui           2026-10-21 18:35:09 +0300  6)     if c == '+':

12fca69 (strohui           2026-10-21 18:35:09 +0300  7)         print(a + b)

0000000 (Not Committed Yet 2026-10-21 18:52:57 +0300  8)     elif c == '-' or c == '-':

eba375b (strohui           2026-10-21 18:36:14 +0300  9)         print(a - b)

c80ed97 (strohui           2026-10-21 18:36:48 +0300 10)     else:

c80ed97 (strohui           2026-10-21 18:36:48 +0300 11)         print(a\*b)

12fca69 (strohui           2026-10-21 18:35:09 +0300 12)

12fca69 (strohui           2026-10-21 18:35:09 +0300 13)

12fca69 (strohui           2026-10-21 18:35:09 +0300 14)

69a090d (strohui           2026-10-20 13:16:27 +0300 15) else:

69a090d (strohui           2026-10-20 13:16:27 +0300 16)     print('Введена неверная операция')





git restore позволяет вернуть файл в последнее состояние, добавление source позволяет вернуть файл до состояния закрепленного в указываемом коммите 

