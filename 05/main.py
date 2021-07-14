# 邮箱

import yagmail

mail = yagmail.SMTP('CA15546466860@126.com', 'TTUHLTNQWFXVZNMI', 'smtp.126.com')
# 发件邮箱 认证码 服务器

word = 'hello,smtp'
# 正文

title = 'good'
# title

mail.send('2528357431@qq.com', title, word)
