# ALTR-Backend

## res codes
- 0 = successful
- 1000 = incorrect UID (ie UID does not own email specified)
- 2000 = non-existent email
- 3000 = non-existent UID
- 4000 = no more emails (domains have ran out)
- 5000 = alias limit reached for user

## altr.cf/create (Create an Alias)
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

## altr.cf/on (Turn on an Alias)
input
```
{
"youremail":"example@example.com",
"email":"google12348@altr1.cf",
"uid":"AFJNJSA70ASFKSAFD80"
}
```
output
```
{
"res":0
}
```

## altr.cf/off (Turn off an Alias)
input
```
{
"youremail":"example@example.com",
"email":"google12348@altr1.cf",
"uid":"AFJNJSA70ASFKSAFD80"
}
```
output
```
{
"res":0
}
```

## altr.cf/status (Turn off an Alias)
input
```
{
"youremail":"example@example.com",
"email":"google12348@altr1.cf",
"uid":"AFJNJSA70ASFKSAFD80"
}
```
output (status will be on or off)
```
{
"status":"on",
"res":0
}
```

## altr.cf/emails (Turn off an Alias)
input
```
{
"youremail":"example@example.com",
"uid":"AFJNJSA70ASFKSAFD80"
}
```
output (status will be on or off)
```
{
"emails":["google12348@altr1.cf","facebook12431@altr1.cf"],
"res":0
}
```
