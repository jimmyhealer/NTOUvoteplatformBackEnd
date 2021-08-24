# NTOUvoteplatform
Creat account:<br />
  `http POST 127.0.0.1:8000/auth/signup/ username="dian" name="dian" password="dian"`<br />
Login command: <br />
  `http --session=loggin-in -a username:password method url request` <br />
Usage of nested json for creating a vote event: <br />
  `http --session=loggin-in -a username:password POST 127.0.0.1:8000/vote/ title="test" content="test" questions:='[{"title": "test", "choices": '['{"choice_text": "agree", "vote": "0"}']'}, {"title": "sdjflkasjdf", "choices": '['{"choice_text": "disagree", "vote": "0"}']'}]'`
