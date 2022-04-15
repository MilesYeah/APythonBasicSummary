
#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__title__  = 操作配置文件工具类
"""

import configparser


class ConfigUtil:
    # 实例化configparser
    config = configparser.ConfigParser()

    def read(self, filename):
        """
        读取配置文件
        :param filename: 配置文件路径
        """
        self.config.read(filename, encoding="utf-8-sig")

    def get(self, _options, _section='server'):
        """
        获取某个options值
        :param _options: option
        :param _section: section
        """
        try:
            # 方式一：调用方法
            value = self.config.get(section=_section, option=_options, fallback="默认值,key不存在则返回此值")

            # 方式二：索引
            value = self.config[_section][_options]
        except Exception as e:
            print("没有获取到值")
            value = None
        return value

    def get_options_key_value(self, _section):
        """
        以列表(name,value)的形式返回section中的每个值
        :param _section: 某个section
        :return: list[tuple(key,value)]
        """
        return self.config.items(_section)

    def get_all_section(self):
        """
        获取所有section
        """
        return self.config.sections()

    def get_options_by_section(self, _section):
        """
        获取section下所有可用options
        """
        # 方式一
        keys = []
        for _options in self.config[_section]:
            keys.append(_options)

        # 方式二（推荐）
        keys = self.config.options(_section)
        return keys

    def assert_section_in_config(self, _section):
        """
        判断section是否存在
        :param _section: 需要判断的section
        """
        return _section in self.config

    def assert_options_in_section(self, _section, _options):
        """
        判断options是否存在某个section中
        :param _section: 某个section
        :param _options: 需要判断的options的key值
        """
        return _options in self.config[_section]


configUtil = ConfigUtil()

if __name__ == '__main__':
    filename = 'F:/imocInterface/config/server.ini'
    configUtil.read(filename)
    print(configUtil.get("username"))
    print(configUtil.get_all_section())
    print(configUtil.assert_section_in_config("server"))
    print(configUtil.get_options_by_section("server"))
    print(configUtil.assert_options_in_section("server", "usernsame"))
    print(configUtil.get_options_key_value("server"))


