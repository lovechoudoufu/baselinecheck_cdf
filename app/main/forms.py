from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp


class LinuxForm(FlaskForm):
    formip = StringField('服务器IP地址', validators=[DataRequired(message='不能为空'), Regexp(
        regex="^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$", message="IP地址")])

    formport = StringField('SSH服务端口', validators=[DataRequired(message='不能为空'), Length(0, 5, message='长度不正确'),
                                                  Regexp(regex="\d+", message="端口必须是数字")])

    formuser = StringField('账户', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    formpwd = StringField('密码', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    formnote = StringField('备注', validators=[DataRequired(message='不能为空'), Length(0, 100, message='长度不正确')])
    submit = SubmitField('提交')


class WindowsForm(FlaskForm):
    formip = StringField('服务器IP地址', validators=[DataRequired(message='不能为空'), Regexp(
        regex="^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$", message="IP地址")])
    formport = StringField('SMB服务器端口(默认445无需修改)', render_kw={'readonly': True},
                           validators=[DataRequired(message='不能为空'), Length(0, 5, message='长度不正确'),
                                       Regexp(regex="\d+", message="端口必须是数字")])
    formuser = StringField('账户', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    formpwd = StringField('密码', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    formnote = StringField('备注', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    submit = SubmitField('提交')


class UploadForm(FlaskForm):
    formfile = FileField('请上传zip压缩包', validators=[FileRequired(), FileAllowed(['zip'])])
    formnote = StringField('备注', validators=[DataRequired(message='不能为空'), Length(0, 64, message='长度不正确')])
    submit = SubmitField()


class ResetpwdForm(FlaskForm):
    oldpwd = StringField('原密码', validators=[DataRequired(), Length(8, 16), ])
    newpwd = StringField('新密码', validators=[DataRequired(), Length(8, 16, message='密码长度需大于8位小于16位'), ])

    submit = SubmitField('提交')
