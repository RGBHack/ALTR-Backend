# ALTR-Backend

## Res codes
0 = successful<br>
1000 = incorrect UID (ie UID does not own email specified) <br>
2000 = non-existent email <br>
3000 = non-existent UID <br>
4000 = no more emails (domains have ran out) <br>
5000 = too many emails for user

## altr.cf/create
Post Request to Backend Service
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
