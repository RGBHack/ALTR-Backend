# ALTR-Backend

## Response (res) Codes

- 0 = successful
- 1000 = incorrect UID (ie UID does not own email specified)
- 2000 = non-existent email
- 4000 = no more emails (domains have ran out)
- 5000 = alias limit reached for user

## Sending a POST request

```javascript
jQuery.ajax({
  url: 'http://URL',
  type: 'POST',
  data: JSON.stringify({
    field1: 'data1',
    field2: 'data2',
  }),
  contentType: 'application/json',
  beforeSend: function(x) {
    if (x && x.overrideMimeType) {
      x.overrideMimeType('application/json;charset=UTF-8')
    }
  },
  success: function(result) {
    var FIELD = result.FIELD
  },
})
```

## Create an Alias (altr.cf/create)

#### Input

```json
{
  "youremail": "example@example.com",
  "uid": "AFJNJSA70ASFKSAFD80",
  "name": "google"
}
```

#### Output

```json
{
  "email": "google12348@altr1.cf",
  "res": 0
}
```

## Turn on an alias (altr.cf/on)

#### Input

```json
{
  "youremail": "example@example.com",
  "email": "google12348@altr1.cf",
  "uid": "AFJNJSA70ASFKSAFD80"
}
```

#### Output

```json
{
  "res": 0
}
```

## Turn off an alias (altr.cf/off)

#### Input

```json
{
  "youremail": "example@example.com",
  "email": "google12348@altr1.cf",
  "uid": "AFJNJSA70ASFKSAFD80"
}
```

#### Output

```json
{
  "res": 0
}
```

## Get an alias' status (altr.cf/status)

#### Input

```json
{
  "youremail": "example@example.com",
  "email": "google12348@altr1.cf",
  "uid": "AFJNJSA70ASFKSAFD80"
}
```

#### Output (on/off)

```json
{
  "status": "on",
  "res": 0
}
```

## Get all aliases (altr.cf/emails)

#### Input

```json
{
  "youremail": "example@example.com",
  "uid": "AFJNJSA70ASFKSAFD80"
}
```

#### Output

```json
{
  "emails": {"google12348@altr1.cf":"off", "facebook12431@altr1.cf":"on"},
  "res": 0
}
```

## Delete an alias (altr.cf/delete)

#### Input

```json
{
  "email": "google1234@altr1.cf",
  "uid": "AFJNJSA70ASFKSAFD80"
}
```

#### Output

```json
{
  "res": 0
}
```
