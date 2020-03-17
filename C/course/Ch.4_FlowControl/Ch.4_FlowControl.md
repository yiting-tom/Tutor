[toc]

# 流程控制

## 1. if-else 敘述
1.  基本語法(main0.c)
> ``` c
> if (條件句) 
>     陳述句1;
> else
>     陳述句2;
> ```
2.  else-if-else語法(main1.c)
> ``` c
> if (條件句) {
>     陳述句1;
>     陳述句2;
> } else if (條件句二) {
>     陳述句3;
>     陳述句4;
> } else {
>     陳述句5;
>     陳述句6;
> }
> ```

## 2. switch 敘述
1. 基本語法(main2.c)
> ``` c
> switch (變數名稱或運算式) { 
>     case 符合數字或字元: 
>         陳述句一; 
>         break; 
>     case 符合數字或字元: 
>         陳述句二; 
>         break; 
>     default: 
>         陳述句三; 
> }
> ```

## 3. for 敘述
1. 基本語法(main3.c)
> ``` c
> for (初始變數; 判斷式; 遞增式) { 
>     陳述句一; 
>     陳述句二; 
> }
> ```

## 4. while 敘述
1. 基本語法(main4.c)
> ``` c
> while(條件式) { 
>     陳述句一; 
>     陳述句二; 
> }
> ```

2. do-while語法(main5.c)
> ``` c
> do { 
>     陳述句一; 
>     陳述句二; 
>     .... 
> } while(條件式);
> ```

## 5. break, continue, goto
1. break
> 離開目前 switch、for、while、do while 的區塊
2. continue
> 的作用與 break 類似，主要使用於迴圈，所不同的是 break 會結束區塊的執行，而 continue 只會結束接下來區塊中的陳述句，並跳回迴圈區塊的開頭繼續下一個迴圈，而不是離開迴圈