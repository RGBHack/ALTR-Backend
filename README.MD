# ALTR-Backend

## res codes
<ul>
  <li>0 = successful</li>
  <li>1000 = incorrect UID (UID does not own the email specified)</li>
  <li>2000 = non-existent email</li>
  <li>3000 = non-existent UID</li>
  <li>4000 = no more emails (domains have ran out)</li>
  <li>5000 = alias limit reached for user's account</li>
<ul>

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
