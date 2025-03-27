
GET

```
$ powershell -ExecutionPolicy Bypass -File "D:\Desktop\Systems\GitHub\rsfact\demo-hinban-master\frontend\excel\mx1_connector.ps1" -method GET -item_id 1
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

POST
```
$ powershell -ExecutionPolicy Bypass -File "D:\Desktop\Systems\GitHub\rsfact\demo-hinban-master\frontend\excel\mx1_connector.ps1" -method 
POST -json_data '{"ex_id": "123", "in_id": "456"}'
{
    "data":  [
                 {
                     "id":  5,
                     "ex_id":  "123",
                     "in_id":  "456"
                 }
             ],
    "errors":  [

               ]
}
```
