# Django Translation Learning

django.utils 의 translation을 활용하여 다양한 언어 대응

1. 번역이 필요한 문장들 중 view와 같이 실행중 적용되는 문장들은 django.utils.translation의 gettext로 감싸 준다.
2. 번역이 필요한 문장들 중 settings와 같이 처음 한번 결정되는 문장들은 django.utils.translation 의 gettext_lazy로 감싸준다.

```class:lineno
from django.utils.translation import 
``` 