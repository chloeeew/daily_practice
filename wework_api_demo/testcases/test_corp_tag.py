"""
==================
Author:Chloeee
Time:2021/7/26 13:20
Contact:403505960@qq.com
==================
"""
import pytest
from api.externalcontact.corp_tag import CorpTag


@pytest.mark.usefixtures("init_corp_tag")
class TestCorpTag:
    def test_smoke_success(self):
        """
        冒烟测试：管理企业标签全流程
        1、获取现存tag
        2、添加tag（数字+中英文）及顺带添加组（数字+中英文+字符）
        3、在添加的组下再次添加tag,order=3
        4、编辑tag,更改为（中+字符）
        5、删除1个tag
        6、再删除1个tag使得group被删除
        """
        ct = CorpTag()
        # 获取当前所有tag,默认存在组客户等级，以及tag名一般
        search_result_01 = ct.search_tag()
        assert "客户等级" in ct.get_groups_name(search_result_01)
        assert "一般" in ct.get_tags_name(search_result_01)

        # 添加tag：冒烟tag1，组名：冒烟组GROUP2!
        ct.add_tag([{"name":"冒烟tag1"}],group_name="冒烟组GROUP2!")
        search_result_02 = ct.search_tag()
        assert "冒烟tag1" in ct.get_tags_name(search_result_02)
        assert "冒烟组GROUP2!" in ct.get_groups_name(search_result_02)
        tag_01_id = ct.get_tags_id_by_name(search_result_02,"冒烟tag1")[0]
        group_id = ct.get_groups_tag_id_by_name(search_result_02,"冒烟组GROUP2!")[0]


        # 在添加的组下再次添加tag,order=3
        # get_order_by_name
        ct.add_tag([{"name":"冒烟弼","order":3}],group_id=group_id)
        search_result_03 = ct.search_tag()
        assert "冒烟弼" in ct.get_tags_name(search_result_03)
        assert 3 == ct.get_orders_by_name(search_result_03,"冒烟弼")[0]
        tag_02_id = ct.get_tags_id_by_name(search_result_03,"冒烟弼")[0]

        # 编辑tag,更改为（中+字符）
        ct.edit_tag(id=tag_02_id,name="冒烟莪@#￥")
        search_result_04 = ct.search_tag()
        assert "冒烟莪@#￥" in ct.get_tags_name(search_result_04)


        # 删除1个tag，group还在
        ct.delete_tag([tag_01_id])
        search_result_05 = ct.search_tag()
        assert tag_01_id not in ct.get_tags_id(search_result_05)
        assert "冒烟组GROUP2!" in ct.get_groups_name(search_result_05)

        # 再删除1个tag使得group被删除
        ct.delete_tag([tag_02_id])
        search_result_06 = ct.search_tag()
        assert tag_02_id not in ct.get_tags_id(search_result_06)
        assert "冒烟组GROUP2!" not in ct.get_groups_name(search_result_06)

    def test_add_tag(self):
        pass







