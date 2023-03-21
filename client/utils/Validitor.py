import re

class FormValidator:
    @staticmethod
    def validate_phone_number(number):
        """
        验证手机号码
        :param number: 待验证的手机号码
        :return: 如果手机号码格式正确，返回True；否则，返回False
        """
        pattern = re.compile(r'^1[3-9]\d{9}$')
        return pattern.match(number) is not None

    @staticmethod
    def validate_email(email):
        """
        验证电子邮件地址
        :param email: 待验证的电子邮件地址
        :return: 如果电子邮件地址格式正确，返回True；否则，返回False
        """
        pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        return pattern.match(email) is not None

    @staticmethod
    def validate_not_empty(text):
        """
        验证文本不为空
        :param text: 待验证的文本
        :return: 如果文本不为空，返回True；否则，返回False
        """
        return text is not None and len(text.strip()) > 0

    @staticmethod
    def validate_text_length(text, min_length=None, max_length=None):
        """
        验证文本长度是否在指定范围内
        :param text: 待验证的文本
        :param min_length: 允许的最小长度
        :param max_length: 允许的最大长度
        :return: 如果文本长度在指定范围内，返回True；否则，返回False
        """
        if min_length is not None and len(text) < min_length:
            return False
        if max_length is not None and len(text) > max_length:
            return False
        return True

    @staticmethod
    def validate_is_number(text):
        """
        验证是否为数字
        :param text: 待验证的文本
        :return: 如果为数字，返回True；否则，返回False
        """
        return text.isdigit()

    @staticmethod
    def validate_is_age(text,min_age=0,max_age=150):
        """
        验证是否为年龄
        :param text: 待验证的文本
        :param min_age: 允许的最小年龄
        :param max_age: 允许的最大年龄
        :return: 如果为年龄，返回True；否则，返回False
        """
        if text.isdigit() == False:
            return False
        age = int(text)
        if age < min_age or age > max_age:
            return False
        return True




