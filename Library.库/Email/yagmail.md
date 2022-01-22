# yagmail

```yaml
# settings.yaml
email:
  # 发件人邮箱
  user:  123456.com
  # 发件人邮箱授权码
  password:  ASGCSFSGS
  # 邮箱host
  host:  smtp.163.com
  contents:  解压apiAutoReport.zip(接口测试报告)后，请使用已安装Live Server 插件的VsCode，打开解压目录下的index.html查看报告
  # 收件人邮箱
  addressees:  ["收件人邮箱1", "收件人邮箱2"]
  title:  接口自动化测试报告(见附件)
  # 附件
  enclosures: report.zip
```



```py
import yagmail
import zipfile
import os
import yaml

with open("settings.yaml", encoding='utf8') as f:
    r = f.read()
    d = yaml.load(r, Loader=yaml.FullLoader)
    pass


class EmailServe:

    @staticmethod
    def zip_report(file_path: str, out_path: str):
        """
        压缩指定文件夹
        :param file_path: 被压缩的文件夹路径
        :param out_path: 生成的压缩文件名
        :return: 无
        """
        zip = zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED)
        for path, dirnames, filenames in os.walk(file_path):
            # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
            fpath = path.replace(file_path, '')

            for filename in filenames:
                zip.write(
                    os.path.join(
                        path, filename), os.path.join(
                        fpath, filename))
        zip.close()

    @staticmethod
    def send_email(setting: dict, file_path):
        """
        入参一个字典
        :param user: 发件人邮箱
        :param password: 邮箱授权码
        :param host: 发件人使用的邮箱服务 例如：smtp.163.com
        :param contents: 内容
        :param addressees: 收件人列表
        :param title: 邮件标题
        :param enclosures: 附件列表
        :param file_path: 需要压缩的文件夹
        :return:
        """
        EmailServe.zip_report(
            file_path=file_path,
            out_path=setting['enclosures'])
        yag = yagmail.SMTP(
            setting['user'],
            setting['password'],
            setting['host'])
        # 发送邮件
        yag.send(
            setting['addressees'],
            setting['title'],
            setting['contents'],
            setting['enclosures'])
        # 关闭服务
        yag.close()


if __name__ == '__main__':
    # EmailServe.zip_report('.', 'report.zip')
    EmailServe.send_email(d['email'], file_path='.')

```
