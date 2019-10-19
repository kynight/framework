#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from framework.utils import logger

class Email(object):
    def __init__(self, server, sender, password, receiver, title, message=None, path=None):
        """
        :@title: 邮件标题，必填。
        :@message: 邮件正文，非必填。
        :@server: smtp服务器，必填。
        :@sender: 发件人，必填。
        :@password: 发件人密码，必填。
        :@receiver: 收件人，多收件人用“；”隔开，必填。
        :@path: 附件路径，可传入list（多附件）或str（单个附件），非必填。
        """
        self.title = title
        self.message = message
        self.files = path
        self.msg = MIMEMultipart('related')
        self.server = server
        self.sender = sender
        self.password = password
        self.receiver = receiver

    def _attach_file(self, att_file):
        att = MIMEText(open('%s' % att_file, 'rb').read(), 'plain', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        file_name = os.path.basename(att_file)
        att["Content-Disposition"] = 'attachment; filename="%s"' % file_name
        self.msg.attach(att)
        logger.info('attach file {}'.format(att_file))

    def send(self):
        self.msg['Subject'] = self.title
        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver

        if self.message:
            self.msg.attach(MIMEText(self.message))

        if self.files:
            if isinstance(self.files, list):
                for f in self.files:
                    self._attach_file(f)
            elif isinstance(self.files, str):
                self._attach_file(self.files)

        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.server)
        except (gaierror ,error) as e:
            logger.exception('发送邮件失败,无法连接到SMTP服务器，检查网络以及SMTP服务器. %s', e)
        else:
            try:
                smtp.login(self.sender, self.password)
            except smtplib.SMTPAuthenticationError as e:
                logger.exception('用户名密码验证失败！%s', e)
            else:
                smtp.sendmail(self.sender, self.receiver.split(';'), self.msg.as_string())
            finally:
                smtp.quit()
                logger.info('发送邮件"{0}"成功! 收件人：{1}。如果没有收到邮件，请检查垃圾箱，'
                            '同时检查收件人地址是否正确'.format(self.title, self.receiver))




