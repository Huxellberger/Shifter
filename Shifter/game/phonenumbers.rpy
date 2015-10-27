label phonenumbers:
  
  python:
    api = clockwork.API("6969f3032679fd68591768d4187fb280a6ea9f57")
    message = clockwork.SMS( to = phonenumber, message = text )
    response = api.send(message)

    if response.success:
      print (response.id)
    else:
      print (response.error_code)
      print (response.error_description)

  return
