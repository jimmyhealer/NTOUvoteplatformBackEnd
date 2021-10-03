# NTOUvoteplatform
Creat account:<br />
  `http POST 127.0.0.1:8000/auth/signup/ username="test" name="test" password="test"`<br />
Login command: <br />
  `http --session=loggin-in -a test:test method url request` <br />
Create vote event: <br />
  1.http:
  `http --session=loggin-in -a test:test POST 127.0.0.1:8000/vote/ title="test" content="test" questions:='[{"title": "test", "choices": '['{"choice_text": "agree", "vote": "0"}']'}, {"title": "sdjflkasjdf", "choices": '['{"choice_text": "disagree", "vote": "0"}']'}]'`<br />
  2.postman:
  ```json
  {
    "title": "test",
    "content": "test",
    "questions": 
    [
        {
            "title": "test",
            "choices":
            [
                {
                    "choice_text": "agree"
                }
            ]
        },
        {
            "title": "sdjflkasjdf",
            "choices":
            [
                {
                    "choice_text": "disagree"
                }
            ]
        }
    ],
    "isPublish": "false",
    "published": "2021-01-01 00:00:00" 
}
```
