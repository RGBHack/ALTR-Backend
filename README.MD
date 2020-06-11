# ALTR-Backend

## res codes
0 = successful
1000 = incorrect UID (ie UID does not own email specified)
2000 = non-existent email
3000 = non-existent UID
4000 = no more emails (domains have ran out)
5000 = too many emails for user

## altr.cf/create
input
```
{
"youremail":"example@example.com",
"uid":"AFJNJSA70ASFKSAFD80",
"name":"gmail"
}
```
output
```
{
"email":"google12348@altr1.cf",
"res":0
}
```
