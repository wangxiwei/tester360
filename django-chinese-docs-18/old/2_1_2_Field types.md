<!--
  ���ߣ�WrongWay [www.wrongway.me]
-->

# Model �ֶβο� #

���ĵ��������� �ֶ�ѡ�� (field options) ���ڲ�ϸ�ں� Django �Ѿ��ṩ�� field types ��

> �μ�
> 
> ������õ��ֶβ����������Ӧ�ã�����Ժ����׵�If the built-in fields don��t do the trick, you can easily ��д�Զ��� model �ֶ� (write your own custom model fields)��

> ע��
> 
> �Ӽ����Ͻ��� model �Ƕ����� django.db.models.fields ���棬��Ϊ��ʹ�÷��㣬���Ǳ����뵽 django.db.models �У���׼�ϣ����ǵ��� from django.db import models ��Ȼ��ʹ�� models.<Foo>Field ����ʽʹ���ֶΡ�

## �ֶ�ѡ�� ##

���в����������ֶ����Ͷ�����Ч�ģ�ͬʱ��Щ����Ҳ�ǿ�ѡ�ġ�

### null ###

**Field.null**

���Ϊ True ��Django �ͻὫ��ֵ(empty)�洢Ϊ���ݿ��е� NULL ��Ĭ��ֵ�� False��

Ҫע����ַ���(empty string)���Ǳ��洢Ϊ���ַ����������� NULL�� null=True ֻ�Է��ַ����ֶ������壬��������(integer)������ֵ(boolean)������(dates)�������������ύ��ֵ�������������ֶΣ��㻹Ҫ������ blank=True ��������Ϊ null ����Ӱ�����ݿ�洢 (��� blank)��

�������кܳ�ֵ����ɣ�����Ҫ���ַ����ֶ�(����CharField �� TextField)��ʹ�� null �����ַ����ֶ������� null=True ������ζ������������Ŀ�ֵ��NULL���Ϳ��ַ���(empty string)�����������£��������ֿ�ֵ�Ƕ���ġ�Django ��������ʹ�ÿ��ַ��������� NULL ��

> ע��
> 
> ��ʹ�� Oracle ���ݿ�ʱ��null=True ѡ���ǿ�ӵ��п����ǿ�ֵ���ַ����ֶΣ����һ������ݿ��б��� NULL ������ʾ���ַ�����

### blank ###

** Field.blank **

���Ϊ True���ֶ������Ĭ��Ϊ False ��

Ҫע���ѡ���� null ��ͬ�� null ���������ݿⷶ��ĸ���� blank ��������֤����ġ����ĳ���ֶ������� blank=True����ô Django �Ĺ����̨��������ֶ���д��ֵ�������������Ϊ blank=False�����ֶξ��Ǳ���ġ�

### choices ###

**Field.choices**

����һ���ɵ����Ķ�Ԫ��(���磬�б����Ԫ��)���������ֶ��ṩѡ���

��������� choices ��Django �Ĺ����̨�ͻ���ʾѡ��򣬶����Ǳ�׼���ı��򣬶������ѡ����ѡ����� choices �е�Ԫ�顣

����һ�� choices �б�����ӣ�

```
YEAR_IN_SCHOOL_CHOICES = (
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
)
```

ÿ��Ԫ���еĵ�һ��Ԫ�أ��Ǵ洢�����ݿ��е�ֵ���ڶ���Ԫ���Ǹ�ѡ���������������

choices �б���Զ���Ϊ model ���һ���֣�

```
class Foo(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
```

Ҳ���Զ����� model ��֮�⣺

```
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)
class Foo(models.Model):
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
```

��Ҳ���Խ� choices ����������飬����������������ṹ��������

```
MEDIA_CHOICES = (
    ('Audio', (
            ('vinyl', 'Vinyl'),
            ('cd', 'CD'),
        )
    ),
    ('Video', (
            ('vhs', 'VHS Tape'),
            ('dvd', 'DVD'),
        )
    ),
    ('unknown', 'Unknown'),
)
```

ÿ��Ԫ���еĵ�һ��Ԫ�ػ���������������ڶ���Ԫ����һ���ɵ����Ķ�Ԫ�飬ÿ����Ԫ�鶼����һ��һ��ֵ��һ��������������������ѡ����Ժ�δ����ѡ�������һ���������б���(���������е� unknown ��)��

Djanog ��������� choices ���ֶ����һ������������������ݸ��ֶεĵ�ǰֵ��ȡ����������������������ݿ� API �ĵ��е� get_FOO_display() ��

���ע��һ�㣬choices �������κοɵ����Ķ��󣬲�������ֻ���б����Ԫ�顣����ζ������Թ��춯̬�� choices �����������ͨ�� ForeignKey ʹ��һ���ʺϵ����ݱ������춯̬ choices���Ͼ� choices �����ڱ䶯����ľ�̬���ݡ�

### db_column ###

**Field.db_column**

���ֶ������ݿ�����ʹ�õ������ơ����û��������Django �ͻ��Ը��ֶε�������Ϊ������

�����ƿ����� SQL �����֣�Ҳ���԰�������������� Python �������������ַ����������ַ���������Ϊ Django ����Ļ��������ͱ����������š�

### db_index ###

**Field.db_index**

���Ϊ True������ django-admin.py sqlindexes <sqlindexes> ��Ϊ���ֶ����һ�� CREATE INDEX ��䡣

### db_tablespace ###

**Field.db_tablespace**

�ⲿ������ Django 1.0 �����ģ� ��鿴�汾�ĵ�
������ֶ��������ֶΣ�db_tablespace �ͱ�ʾ���������ڵ����ݿ��ռ�����ơ������Ŀ�����ļ����趨�� DEFAULT_INDEX_TABLESPACE ����ôĬ��ֵ�����������ֵ�������ָ���˸� model �� Meta ��Ƕ��� db_tablespace ����ôĬ��ֵ���� Meta �� db_tablespace ��ֵ��������ݿⲻ֧�ֱ�ռ䣬�ͻ���Ը�ѡ�

## default ##

**Field.default**

���ֶε�Ĭ��ֵ����������һ��ֵ��Ҳ������һ���ɵ��õĶ���(�����֮Ϊ����C)�����Ǻ��ߣ���ôÿ�δ���һ���¶���ʱ������C���������á�

### editable ###

**Field.editable**

���Ϊ False ����ô�� Django �����̨�оͲ���༭���ֶΣ�ͬ������ Django �Զ����ɵı���Ҳ����༭���ֶΡ�Ĭ��ֵ�� True ��

### help_text ###

**Field.help_text**

���ӵ���ʾ��Ϣ���ڹ����̨�༭�ö���ı��У�����ʾ�ڸ��ֶ����档��ʹ��Ķ��������ں�̨���������ĵ���Ҳ�Ǻ��õġ�

ע�⣬�ڹ����̨��ʾ����ʾ��Ϣʱ�����������ת�塣����������� help_text �а��� HTML �����磺

```
help_text="Please use the following format: <em>YYYY-MM-DD</em>."
```

��Ҳ����ʹ�ô��ı����������� django.utils.html.escape() ת���κ� HTML �ַ���

### primary_key ###

**Field.primary_key**

���Ϊ True����ô���ֶξ��� model ��������

�����û��ָ���κ�һ���ֶε� primary_key=True ��Django �ͻ��Զ����һ�� IntegerField ��Ϊ�����ֶΡ����Գ���������дĬ�ϵ�������Ϊ������û��Ҫ���κ��ֶ������� primary_key=True ����� ���������ֶ� (Automatic primary key fields) ��

primary_key=True ��ζ�� null=False �� unique=True ��һ������ֻ����һ��������

### unique ###

**Field.unique**

���Ϊ True�����ֶ�ֵ�ͱ�����ȫ��Ψһ�ġ�

��ͬʱ���������ݿ�㼶�Լ� Django �Ĺ����̨�ͱ��㼶������㱣�� model ʱ��ĳ�� unique �ֶε�ֵ���ظ��ģ���ô save() �����ͻ��׳� django.db.IntegrityError �쳣��

���ѡ�������е��ֶ��϶��ǿ��õģ����� ManyToManyField �� FileField ���⡣

### unique_for_date ###

**Field.unique_for_date**

���Ҫ����ĳ�������ڣ����ֶ�ֵ�����ݱ�����Ψһ��(�Ͳ�����ʱ�ں��ֶ�ֵ����ͬ�ļ�¼)���ǾͿ��Խ� unique_for_date ����Ϊĳ�� DateField �� DateTimeField �����ơ�

���磬��������һ�������� unique_for_date="pub_date" �� title �ֶΣ���ô Django �Ͳ���������� title �� pub_date ��ͬ��������¼��

�������� Django �Ĺ����̨�ͱ��㼶���������ݿ�㼶��

### unique_for_month ###

**Field.unique_for_month**

�� unique_for_date ���ƣ�ֻ�����޶������·֡�

### unique_for_year ###

**Field.unique_for_year**

�� unique_for_date�� unique_for_month ���ƣ�ֻ�����޶�������֡�

### verbose_name ###

**Field.verbose_name**

���ֶ������������ơ����û���ṩ��������Django ������ֶε��������Զ�����������--���ǽ����������еĿո��滻���»��ߡ���� �ֶε�������(Verbose field names).

## �ֶ����� ##

### AutoField ###

**class AutoField(\*\*options)**

����һ������ ID �������� IntegerField �ֶΡ�ͨ�����㲻��ֱ��ʹ�ø��ֶΡ������û�ڱ���ֶ���ָ��������Django �ͻ��Զ���������ֶΡ���� ���������ֶ�(Automatic primary key fields)��

### BooleanField ###


**class BooleanField(\*\*options)**

һ������ֵ(true/false)�ֶΡ�

Django �Ĺ����̨��checkbox�����ָ��ֶ����͡�

MySQL �û���ע�⣺

�����ֶ��� MySQL �б��洢Ϊ TINYINT �С�����ֵֻ���� 0 �� 1 (����������ݿⶼ�����õ� BOOLEAN ����)�����Խ���ʹ�� MySQL ������£������ݿ��м��� BooleanField ������Ϊ model �����ԣ���ʱ����ֵ�� 1 ���� 0 �������� True �� False ����������£��ⲻ���������⣬��Ϊ Python ��֤�� 1 == True �� 0 == False ������Ч�ġ�ֻ�������д���� obj is True ���ʱ����� obj ���� model ��һ����������ֵ�������Ҫ����ע���ˡ���Ϊ��ʹ�� mysql ���ݿ�ʱ��"is" ��������Ч�ġ������ֳ����£�ʹ������жϸ���(ʹ�� "==")��

### CharField ###

**class CharField(max_length=None[, \*\*options])**

����һ���ַ����ֶΣ���С�ַ����ʹ��ַ��������á�

���ڸ�����ı���Ӧ��ʹ�� TextField ��

Django �Ĺ����̨�� `<input type="text">` (���������) ����ʾ�����ֶΡ�

CharField ��һ�����봫��Ĳ�����

**CharField.max_length**

�ֶε�����ַ����������������ݿ�㼶�� Django ��������֤�㼶��

> ע��
> 
> ��������ڱ�д��Ӧ��Ҫ������������ݿ⣬��ô���Ҫע�ⲻͬ���ݿ�� max_length �в�ͬ�����ơ���� ���ݿ� (database backend notes) ��

MySQL �û���ע�⣺

�����ʹ�� MySQLdb 1.2.2 �� utf8_bin �ַ���(��Ĭ������)���м���ע������Ҫ�������⡣��� MySQL ���ݿ� (MySQL database notes) ��

### CommaSeparatedIntegerField ###

**class CommaSeparatedIntegerField(max_length=None[, \*\*options])**

����������Զ��ż�����������С��� CharField һ��������Ϊ���ṩ max_length ����������Ҫע�ⲻͬ���ݿ�� max_length �����ơ�

### DateField ###

**class DateField([auto_now=False, auto_now_add=False, \*\*options])**

���ֶ����� Python �� datetime.date ʵ������ʾ���ڡ�������������Ŀ�ѡ������

**DateField.auto_now**

ÿһ�α������ʱ��Django �����Զ������ֶε�ֵ����Ϊ��ǰʱ�䡣һ��������ʾ "����޸�" ʱ�䡣Ҫע��ʹ�õ��ǵ�ǰ���ڣ�������Ĭ��ֵ�������㲻��ͨ����дĬ��ֵ�İ취���ı䱣��ʱ�䡣

**DateField.auto_now_add**

�ڵ�һ�δ�������ʱ��Django �Զ������ֶε�ֵ����Ϊ��ǰʱ�䣬һ��������ʾ���󴴽�ʱ�䡣��ʹ�õ�ͬ���ǵ�ǰ���ڣ�����Ĭ��ֵ��
Django �����̨ʹ��һ������ Javascript ������ <input type="text"> ����ʾ���ֶΣ�������һ����ǰ���ڵĿ��ѡ���Ǹ� JavaScript ������������������Ϊһ�����ڵĵ�һ�졣

### DateTimeField ###

**class DateTimeField([auto_now=False, auto_now_add=False, \*\*options])**

���ֶ����� datetime.datetime ʵ����ʾ���ں�ʱ�䡣���ֶ������ܵĲ����� DateField һ����

Django �Ĺ����̨ʹ������ <input type="text"> �ֱ��ʾ���ں�ʱ�䣬ͬ��Ҳ���� JavaScript ���ѡ�

### DecimalField ###

�ⲿ������ Django 1.0 �������ģ� ��鿴�汾�ĵ�

**class DecimalField(max_digits=None, decimal_places=None[, \*\*options])**

����ʹ�� Decimal ʵ����ʾ�̶����ȵ�ʮ���������ֶΡ�������������Ĳ�����

**DecimalField.max_digits**

������������λ��

**DecimalField.decimal_places**

С�������λ��
���磬Ҫ�洢���������ֵ��999������������С��λ�������ʹ�ã�

```
models.DecimalField(..., max_digits=5, decimal_places=2)
```

Ҫ�洢��Լ��ʮ�ڼ��Ҵ���10��С��λ�����֣�������д��

```
models.DecimalField(..., max_digits=19, decimal_places=10)
```

Django �����̨ʹ�� `<input type="text">` (���������) ��ʾ���ֶΡ�

### EmailField ###

**class EmailField([max_length=75, \*\*options])**

���Ǵ��� email �Ϸ��Լ���A CharField ��

### FileField ###

**class FileField(upload_to=None[, max_length=100, \*\*options])**

�ļ��ϴ��ֶ�

> ע��
> 
> ���ֶβ�֧�� primary_key �� unique ������������׳� TypeError �쳣��

����һ������Ĳ�����

**FileField.upload_to**

���ڱ����ļ��ı����ļ�ϵͳ�������� MEDIA_ROOT ����ȷ�����ļ��� url ���ԡ�

��·�����԰��� ʱ���ʽ�� (strftime formatting)���������ϴ��ļ���ʱ���滻�ɵ�ʱ���ڣ�ʱ��(�������Ͳ���������ϴ��ļ���ĳ��Ŀ¼�����������)��

�� Django 1.0 �ѸĶ��� ��鿴�汾�ĵ�
�ò���Ҳ������һ���ɵ����������һ����ʽ�����Ե��ú�ʽ��ð����ļ������ϴ�·��������ɵ��������Ҫ�����������������ҷ���һ�������ļ��õ� Unix-Style ��·��(�� / б��)�����������ֱ��ǣ�

����������
instance��
�����˵�ǰ FileField �� model ʵ������׼ȷ��˵�������Ը��ļ�Ϊ������ model ʵ����

���������£��ڱ�����ļ�ʱ�� model ʵ�����󻹲�û�б��浽���ݿ⣬������Ϊ�����п���ʹ��Ĭ�ϵ� AutoField������ʱ����û�д����ݿ��л������ֵ��(�÷���oteam��http://oteam.cn/2008/10/4/dynamic-upload-paths-in-django/)

filename���ϴ��ļ���ԭʼ���ơ�����������·����ʱ���п��ܻ��õ�����
����һ����ѡ�Ĳ�����

**FileField.storage**

�ⲿ������ Django 1.0 �������ģ� ��鿴�汾�ĵ�
���𱣴�ͻ�ȡ�ļ��Ķ������ Managing files��

Django �����̨ʹ�� `<input type="file">` (һ���ļ��ϴ��Ĳ���) ����ʾ�������

�� model ��ʹ�� FileField �� ImageField (�Ժ���ᵽ) Ҫ�������µĲ��裺

+ ����Ŀ�����ļ��У���Ҫ���� MEDIA_ROOT ��������ֵ��Ϊ��������ϴ��ļ���Ŀ¼������·����(�������ܵĿ��ǣ�Django û�н��ļ����������ݿ��С�) ��Ȼ���� MEDIA_URL ��������ֵ��Ϊ��ʾ��Ŀ¼����ַ��Ҫȷ�� web ���������õ��ʺ�ӵ�жԸ�Ŀ¼��дȨ�ޡ�
+ �� model ������� FileField �� ImageField ������ȷ���Ѷ����� upload_to ��� Django ֪��Ӧ���� MEDIA_ROOT ���ĸ���Ŀ¼�������ļ���
+ �洢�����ݿ⵱�еĽ���ֻ���ļ���·��(����������� MEDIA_ROOT �����·��)��������Ѿ��뵽���� Django �ṩ�� url �������ĺ�ʽ���ٸ����ӣ������� ImageField ������ mug_shot����ô�������ģ����ʹ�� {{ object.mug_shot.url }} �����ܵõ�ͼƬ��������ַ��

���磬������� MEDIA_ROOT ����Ϊ '/home/media'��upload_to ����Ϊ 'photos/%Y/%m/%d'�� upload_to �е� '%Y/%m/%d' ��һ�� ʱ���ʽ�ַ��� (strftime formatting)�� '%Y' ����λ����֣�'%m' ����λ���·֣� '%d' ����λ�����ӡ��������2007��01��15���ϴ���һ���ļ�����ô����ļ��ͱ����� /home/media/photos/2007/01/15 Ŀ¼�¡�

�������õ��ϴ��ļ��ı����ļ����ƣ��ļ���ַ�������ļ��Ĵ�С�������ʹ�� name, url �� size ���ԣ���� �����ļ� (Managing files)��

ע�⣺���ϴ��ļ�ʱ��Ҫ���豣���ļ���λ�ú��ļ������ͣ���ô����ԭ����Ϊ�˱��ⰲȫ©������ÿһ���ϴ��ļ���Ҫ��֤�����������ȷ���ϴ����ļ�������Ҫ���ļ����ٸ����ӣ������äĿ���ñ����ϴ��ļ�����û�ж��ϴ��ļ�������֤����������ļ���Ŀ¼���� web �������ĸ�Ŀ¼�£���һ�����ϴ���һ�� CGI ���� PHP �ű���Ȼ��ͨ�����ʽű���ַ�������ϴ��Ľű����ǿɾ�̫Σ���ˡ�ǧ��Ҫ�����������鷢����

�ⲿ������ Django 1.0 �������ģ� ������汾�У��¼��� max_length ������
Ĭ������£�FileField ʵ�������ݿ��еĶ�Ӧ���� varchar(100) ���������ֶ�һ������������� max_length �����ı��ֶε���󳤶ȡ�

### FilePathField ###

**class FilePathField(path=None[, match=None, recursive=False, max_length=100, \*\*options])**

����һ�� CharField ��������ѡ���ļ�ϵͳ��ĳ��Ŀ¼�����ĳЩ�ļ�����������ר�еĲ�����ֻ�е�һ�������Ǳ���ģ�

**FilePathField.path**

��������Ǳ���ġ�����һ��Ŀ¼�ľ���·���������Ŀ¼���� FilePathField ����ѡ���ļ����Ǹ�Ŀ¼�����磺 "/home/images".
**FilePathField.match**

��ѡ����������һ��������ʽ�ַ����� FilePathField �����������ļ����ƣ�ֻ�з����������ļ��ų������ļ�ѡ���б��С�Ҫע��������ʽֻƥ���ļ�����������ƥ���ļ�·�������磺 "foo.*\.txt$" ֻƥ����Ϊ foo23.txt ����ƥ�� bar.txt �� foo23.gif��
**FilePathField.recursive**

��ѡ����������ֵ�� True �� False��Ĭ��ֵ�� False����ָ���Ƿ���� path �µ���Ŀ¼��
��Ȼ����������������ͬʱʹ�á�

ǰ���Ѿ��ᵽ�� match ֻƥ���ļ����ƣ��������ļ�·������������������ӣ�

```
FilePathField(path="/home/images", match="foo.*", recursive=True)
```

��ƥ�� /home/images/foo.gif ������ƥ�� /home/images/foo/bar.gif��������Ϊ match ֻƥ���ļ��� (foo.gif �� bar.gif).

�ⲿ������ Django 1.0 �������ģ� ������汾�У��¼��� max_length ������
Ĭ������£� FilePathField ʵ�������ݿ��еĶ�Ӧ����s varchar(100) ���������ֶ�һ������������� max_length �����ı��ֶε��������

### FloatField ###

**class FloatField([\*\*options])**

�� Django 1.0 ���ѸĶ��� ��鿴�汾�ĵ�
���ֶ��� Python ��ʹ��by a float ʵ������ʾһ����������

Django �����̨�� `<input type="text">` (һ�����������) ��ʾ���ֶΡ�

### ImageField ###

**class ImageField(upload_to=None[, height_field=None, width_field=None, max_length=100, \*\*options])**

�� FileField һ����ֻ�ǻ���֤�ϴ������ǲ���һ���Ϸ���ͼ���ļ�������������ѡ������

**ImageField.height_field**

����ͼƬ�߶ȵ��ֶ����ơ��ڱ������ʱ������ݸ��ֶ��趨�ĸ߶ȣ���ͼƬ�ļ���������ת����

**ImageField.width_field**

����ͼƬ��ȵ��ֶ����ơ��ڱ������ʱ������ݸ��ֶ��趨�Ŀ�ȣ���ͼƬ�ļ���������ת����
������Щ�� FileField ����Ч�Ĳ���֮�⣬ ImageField ������ʹ�� File.height and File.width �������ԡ���������ļ� (Managing files)(���Ҹ���wrongway��û���ҵ������������Ľ���)��

ʹ�ø��ֶ�Ҫ��װ Python Imaging Library(PIL).

�ⲿ������ Django 1.0 �������ģ� ���°汾���¼��� max_length ������
Ĭ������£� ImageField ʵ����Ӧ�����ݿ��е� created as varchar(100) �С��������ֶ�һ���������ʹ�� max_length �������ı��ֶε���󳤶ȡ�

### IntegerField ###

**class IntegerField([\*\*options])**

�����ֶΡ�Django �����̨�� `<input type="text">` (һ�����������) ��ʾ���ֶΡ�

### IPAddressField ###

**class IPAddressField([\*\*options])**

���ַ�����ʽ(���� 192.0.2.30)��ʾ IP ��ַ�ֶΡ�Django �����̨ʹ�� `<input type="text">` (һ�����������) ��ʾ���ֶΡ�

### NullBooleanField ###

**class NullBooleanField([\*\*options])**

�� BooleanField ���ƣ�������һ�� NULL ѡ������ø��ֶδ���ʹ�� null=True ѡ��� BooleanField ��Django �����̨ʹ�� `<select>` ѡ�������ʾ���ֶΣ�ѡ���������ѡ��ֱ��� "Unknown", "Yes" �� "No" ��

### PositiveIntegerField ###

**class PositiveIntegerField([\*\*options])**

�� IntegerField ���ƣ����ֶ�ֵ�����ǷǸ�����

### PositiveSmallIntegerField ###

**class PositiveSmallIntegerField([\*\*options])**

�� PositiveIntegerField ���ƣ�����ֵ��ȡֵ��Χ��С�����������ݿ����á�

### SlugField ###

**class SlugField([max_length=50, \*\*options])**

Slug ��һ�����������ָĳ���¼��Ķ̱�ǩ����ֻ������ĸ�����֣��»��߻����ַ���ɡ�ͨ������£�����������ַ��һ���֡�

�� CharField ���ƣ������ָ�� max_length (Ҫע�����ݿ�����Ժͱ����ᵽ�� max_length )�����û��ָ�� max_length ��Django ��Ĭ���ֶγ���Ϊ50��

���ֶλ��Զ����� Field.db_index to True��

���������ֶε�ֵ���Զ���� Slug �ֶ��Ǻ����õġ�������� Django �Ĺ����̨��ʹ�� prepopulated_fields ��������һ�㡣

### SmallIntegerField ###

**class SmallIntegerField([\*\*options])**

�� IntegerField ���ƣ�����ֵ��ȡֵ��Χ��С�����������ݿ�����ơ�

### TextField ###

**class TextField([\*\*options])**

���ı��ֶΡ�Django �Ĺ����̨ʹ�� `<textarea>` (һ�������ı���) ��ʾ���ֶΡ�

MySQL �û���ע��

���������ʹ�� MySQLdb 1.2.1p2 �� utf8_bin �ַ���(��Ĭ������)���м���ע������Ҫ�������⣬��� MySQL database notes ��

### TimeField ###

**class TimeField([auto_now=False, auto_now_add=False, \*\*options])**

���ֶ�ʹ�� Python �� datetime.time ʵ������ʾʱ�䡣���� DateField ����ͬ�����Զ����Ĳ�����

Django �����̨ʹ��һ���� Javascript ������� �� `<input type="text">` ��ʾ���ֶΡ�

### URLField ###

**class URLField([verify_exists=True, max_length=200, \*\*options])**

���� URL �� CharField ������һ������Ŀ�ѡ������

**URLField.verify_exists**

���Ϊ True (Ĭ��ֵ)��Django �ڱ������ʱ����� URL �Ƿ�ɷ���(���磬��ַ�����������ʣ�������404����)��ֵ��ע����ǣ������ʹ�õ���һ�����߳̿�������������ô��֤��ַ�����ǰ�̡߳���Ȼ�����������õĶ��̷߳�������˵����Ͳ���һ�������ˡ�
Django �����̨ʹ�� `<input type="text">` (һ�����������) ��ʾ���ֶΡ�

������ CharField ����һ����URLField ���ܿ�ѡ�� max_length �������ò���Ĭ��ֵ��200��

### XMLField ###

**class XMLField(schema_path=None[, \*\*options])**

����һ�����ݸ����� schema ��֤�����ı��Ƿ��ǺϷ� XML �� TextField �ֶΡ�����һ������Ĳ�����

**schema_path**

������֤ XML �� RelaxNG schema ���ļ�·����
������ϵ�ֶ� (Relationship fields)

Django Ҳ������һ��������ʾ������ϵ���ֶΡ�

### ForeignKey ###

**class ForeignKey(othermodel[, \*\*options])**

����һ�����һ��ϵ������Ϊ���ṩһ��λ�ò������������� model �ࡣ

Ҫ�����ݹ����ʱ--������Լ������һ��ϵ���Ǿ�ʹ�� models.ForeignKey('self') ��

�����Ҫ��ĳ����δ����� model �������� ����ʹ�� model �����ƣ�������ʹ�� model ������

```
class Car(models.Model):
    manufacturer = models.ForeignKey('Manufacturer')
    # ...

class Manufacturer(models.Model):
    # ...
```

�ⲿ������ Django 1.0 ���½��ģ� ��鿴�汾�ĵ�
Ҫ������Ӧ���е� model ���������Ҫ��������Ӧ�ñ�ǩ����ʽ�ض�����������磬�������� Manufacturer model ����������һ����Ϊ production ��Ӧ���У���ֻҪ�ã�

```
class Car(models.Model):
    manufacturer = models.ForeignKey('production.Manufacturer')
```

�ڽ������Ӧ��˫������ʱ���������÷����ǳ����á�

#### ���ݿ���� ####

Django ʹ�ø��ֶ����ƣ� "_id" ��Ϊ���ݿ��е������ơ�������������У� Car model ��Ӧ�����ݱ��л���һ�� manufacturer_id �С�(�����ͨ����ʽ��ָ�� db_column ���ı���ֶε�������)�����������������Զ��� SQL ������û��Ҫ�������ݿ�������ơ�

#### ���� ####

ForeignKey ����������Щ��ѡ��������Щ���������˹�ϵ��������еġ�

**ForeignKey.limit_choices_to**

����һ������ɸѡ�����Ͷ�Ӧֵ���ֵ� (���see ������ѯ(Making queries))�������� Django �����̨ɸѡ�����������磬���� Python �� datetime ģ�飬���˵�������ɸѡ������������

```
limit_choices_to = {'pub_date__lte': datetime.now}
```

ֻ�� pub_date �ڵ�ǰ����֮ǰ�Ĺ������������ѡ��

Ҳ����ʹ�� Q �����������ֵ䣬�Ӷ�ʵ�ָ����ӵ�ɸѡ����� ���Ӳ�ѯ (complex queries)��

limit_choices_to �����ڹ����̨��ʾΪ inline �Ĺ������������á�

**ForeignKey.related_name**

�������ƣ������ӱ������ֶ�ָ������ֶΡ��� �����������ĵ� (related objects documentation) ������ϸ���ܺͷ�����ע�⣬���㶨�� ���� model (abstract models) ʱ���������ʽָ����������; ֻ��������ô����֮�� ĳЩ�ر��﷨ (some special syntax) ��������ʹ�á�
**ForeignKey.to_field**

ָ����ǰ��ϵ�뱻���������е��ĸ��ֶι�����Ĭ������£�to_field ָ�򱻹��������������

### ManyToManyField ###

**class ManyToManyField(othermodel[, \*\*options])**

���������Զ��ϵ���������һ��λ�ò������������� model �ࡣ������ʽ�� ForeignKey һ��, �� �ݹ���� (recursive) and �Ӻ���� (lazy) ��һ����

#### ���ݿ��ʾ  ####

Django ����һ���м������ʾ��Զ��ϵ��Ĭ������£��м���������������ϵ������϶��ɡ�����ĳЩ���ݿ�Ա����ĳ��������ƣ������м������ƻ��Զ�������64���ַ����ڣ�������һ�����ظ��Ĺ�ϣ�ַ���������ζ�ţ�����ܿ������� author_books_9cdf4 �����ı����ƣ����Ǻ������ġ������ʹ�� db_table ѡ���ֶ�ָ���м�����ơ�

#### ����  ####

ManyToManyField �������п�ѡ��������Щ���������˹�ϵ��������еġ�

ManyToManyField.related_name
�� ForeignKey.related_name �÷�һ����
ManyToManyField.limit_choices_to
�� ForeignKey.limit_choices_to �÷�һ����

limit_choices_to ����ͨ�� through ����ָ�����н��� ManyToManyField �������á�

**ManyToManyField.symmetrical**

ֻҪ����ݹ�Ķ�Զ��ϵʱ�����á��ٵ�����������һ�� model :

```
class Person(models.Model):
    friends = models.ManyToManyField("self")
```

Django ����� model ʱ��Django �ᷢ�����һ�������Լ��ĵݹ� ManyToManyField ������ Django ��������ֶ����һ��ָ�� Person ��� person_set ���ԣ����ǰ� ManyToManyField ��Ϊ�ԳƵ�--Ҳ����˵���������������ѣ���ô����ȻҲ�����ҵ����ѡ�

������뽫�ݹ�Ķ�Զ��ϵ��Ϊ�ԳƵģ������ָ�� symmetrical Ϊ False�������ͻ�ǿ�� Django ��ӷ������ƣ��Ӷ����� ManyToManyField ������Ϊ�ǶԳƵġ�

**ManyToManyField.through**

Django ���Զ�����һ�ű��������Զ��ϵ�����ǣ���������ֶ�ָ���м��������� through ѡ����ָ�� model ʹ������ĳ�� model �������Զ��ϵ������� model �����м������Ӧ�� model ��(�ҽ�through��ָ�����м���Ϊ�н��)��

������ʹ�� ��Զ��ϵ�е��������� (extra data with a many-to-many relationship) ʱ��һ��Ҫ�õ����ѡ�

**ManyToManyField.db_table**

ָ�����ݿ��б����Զ��ϵ���ݵı����ơ����û���ṩ��ѡ�Django �ͻ����������ϵ�����������һ���µı�������Ϊ�м������ơ�

### OneToOneField ###

**class OneToOneField(othermodel[, parent_link=False, \*\*options])**

��������һ��һ��ϵ����ͳ�ؽ������������� unique=True �� ForeignKey �ǳ����ƣ���ͬ����ʹ�÷��������ʱ�򣬵õ��Ĳ���һ�������б�����һ�������Ķ���

��ĳ�� model ��չ����һ�� model ʱ������ֶ��Ƿǳ����õģ����磺 ���̳� (Multi-table inheritance) ����ͨ������ model �����һ��ָ�� model ��һ��һ������ʵ�ֵġ�

��������ֶ�һ���������������� model �ࡣ������ʽ�� ForeignKey һ������ �ݹ���� (recursive) �� �Ӻ���� (lazy) ��һ����

���⣬OneToOneField ���� ForeignKey �ɽ��ܵĲ�����ֻ��һ�������� OnetoOneField ר�еģ�

**OneToOneField.parent_link**

���Ϊ True �����������ڼ̳���ĳ���� model ���� model ��(���ﲻ�����Ӻ�̳У��� model ������ʵ����)����ô���ֶξͻ���ָ����ʵ��������(���߽�����)�������������� OneToOneField ����������չ���ಢ�̳и������ԡ�