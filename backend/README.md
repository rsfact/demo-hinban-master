
```
$ powershell -ExecutionPolicy Bypass -File "C:\Users\r1999\Desktop\Systems\rsfact\demo-hinban-master\backend\mx1_connector.ps1" -method GET -item_id 1

data                                                     errors
----                                                     ------
{@{id=1; ex_id=tb_89924-X1175-00; in_id=7880_Color_580}} {}



r1999@rs-gram01 MINGW64 ~/Desktop/Systems/rsfact/demo-hinban-master/backend (main)
$ powershell -ExecutionPolicy Bypass -File "C:\Users\r1999\Desktop\Systems\rsfact\demo-hinban-master\backend\mx1_connector.ps1" -method GET -item_id 1
{
    "data":  [
                 {
                     "id":  1,
                     "ex_id":  "tb_89924-X1175-00",
                     "in_id":  "7880_Color_580"
                 }
             ],
    "errors":  [

               ]
}
```
