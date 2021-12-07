from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp

# 定义linux在线检查的表单
class LinuxForm(FlaskForm):
    # 在线检查模式的linux表单
    formip = StringField('服务器IP地址', validators=[DataRequired(message='不能为空'), Regexp(regex="^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$",message="IP地址")])
    # Regexp 函数中通过正则语法限定了写入的ip格式，避免出现错误的ip格式引起代码的报错
    formport = StringField('SSH服务端口', validators=[DataRequired(message='不能为空'), Length(0, 5, message='长度不正确'),Regexp(regex="\d+",message="端口必须是数字")])
    # 同上，使用正则语法限定端口为数字
    formuser = StringField('账户', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    formpwd = StringField('密码', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    formnote = StringField('备注', validators=[DataRequired(message='不能为空'), Length(0, 100, message='长度不正确')])
    submit = SubmitField('提交')

# 定义windows在线检查的表单，内容同linux在线检查
class WindowsForm(FlaskForm):
    # 在线检查模式的windows表单
    formip = StringField('服务器IP地址', validators=[DataRequired(message='不能为空'), Regexp(regex="^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$",message="IP地址")])
    formport = StringField('SMB服务器端口(默认445无需修改)', render_kw={'readonly': True}, validators=[DataRequired(message='不能为空'), Length(0, 5, message='长度不正确'),Regexp(regex="\d+",message="端口必须是数字")])
    formuser = StringField('账户', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    formpwd = StringField('密码', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    formnote = StringField('备注', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    submit = SubmitField('提交')

# 定义文件上传的表单
class UploadForm(FlaskForm):
    formfile = FileField('请上传zip压缩包', validators=[FileRequired(), FileAllowed(['zip'])])
    formnote = StringField('备注', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    submit = SubmitField()

# 定义重置密码的表单
class ResetpwdForm(FlaskForm):
    oldpwd = StringField('原密码', validators=[DataRequired(), Length(8, 16), ])
    newpwd = StringField('新密码', validators=[DataRequired(), Length(8, 16,message='密码长度需大于8位小于16位'), ])
    # 设置新密码参数的限制条件，密码长度需要大于8小于16
    submit = SubmitField('提交')