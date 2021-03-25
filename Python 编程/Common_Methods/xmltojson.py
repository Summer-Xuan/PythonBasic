import json
import xmltodict
# Python中xml和json格式是可以互转的，就像json格式转Python字典对象那样。

def xmltojson(xmlstr):
    """
    parse是xml解析器
    json库dumps()是将dict转化成json格式，loads()是将json转化成dict格式。
    dumps()方法的ident=1，格式化json
    """
    xmlparse = xmltodict.parse(xmlstr)
    jsonstr = json.dumps(xmlparse, ensure_ascii=False, indent=1)
    print(jsonstr)
    with open('../file/pic_template.json', 'w',encoding='utf8') as f:
     f.write(jsonstr)


def jsontoxml(jsonstr):
    """
    xmltodict库的unparse()json转xml
    """
    xmlstr = xmltodict.unparse(jsonstr)
    print(xmlstr)

if __name__ == '__main__':
    xml = '''<annotation>
	<folder>增值税普票</folder>
	<filename>p22.jpg</filename>
	<path>D:/inspur/增值税普票/增值税普票/p22.jpg</path>
	<source>
		<database>Unknown</database>
	</source>
	<size>
		<width>2590</width>
		<height>1644</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>开票日期</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>1875</xmin>
			<ymin>266</ymin>
			<xmax>2056</xmax>
			<ymax>309</ymax>
		</bndbox>
	</object>
	<object>
		<name>货物或应税劳务、服务名称</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>176</xmin>
			<ymin>618</ymin>
			<xmax>662</xmax>
			<ymax>662</ymax>
		</bndbox>
	</object>
	<object>
		<name>规格型号</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>793</xmin>
			<ymin>620</ymin>
			<xmax>969</xmax>
			<ymax>662</ymax>
		</bndbox>
	</object>
	<object>
		<name>单位</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>1069</xmin>
			<ymin>616</ymin>
			<xmax>1149</xmax>
			<ymax>659</ymax>
		</bndbox>
	</object>
	<object>
		<name>数量</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>1247</xmin>
			<ymin>620</ymin>
			<xmax>1358</xmax>
			<ymax>659</ymax>
		</bndbox>
	</object>
	<object>
		<name>单价</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>1489</xmin>
			<ymin>620</ymin>
			<xmax>1610</xmax>
			<ymax>661</ymax>
		</bndbox>
	</object>
	<object>
		<name>金额</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>1769</xmin>
			<ymin>624</ymin>
			<xmax>1921</xmax>
			<ymax>666</ymax>
		</bndbox>
	</object>
	<object>
		<name>税率</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>2043</xmin>
			<ymin>622</ymin>
			<xmax>2126</xmax>
			<ymax>662</ymax>
		</bndbox>
	</object>
	<object>
		<name>税额</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>2245</xmin>
			<ymin>622</ymin>
			<xmax>2401</xmax>
			<ymax>664</ymax>
		</bndbox>
	</object>
	<object>
		<name>合计</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>276</xmin>
			<ymin>1083</ymin>
			<xmax>549</xmax>
			<ymax>1122</ymax>
		</bndbox>
	</object>
	<object>
		<name>价税合计</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>241</xmin>
			<ymin>1159</ymin>
			<xmax>428</xmax>
			<ymax>1203</ymax>
		</bndbox>
	</object>
	<object>
		<name>收款人</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>147</xmin>
			<ymin>1477</ymin>
			<xmax>293</xmax>
			<ymax>1522</ymax>
		</bndbox>
	</object>
	<object>
		<name>复核</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>821</xmin>
			<ymin>1483</ymin>
			<xmax>908</xmax>
			<ymax>1522</ymax>
		</bndbox>
	</object>
	<object>
		<name>开票人</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>1339</xmin>
			<ymin>1481</ymin>
			<xmax>1476</xmax>
			<ymax>1527</ymax>
		</bndbox>
	</object>
	<object>
		<name>销售方</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>0</difficult>
		<bndbox>
			<xmin>1899</xmin>
			<ymin>1481</ymin>
			<xmax>2043</xmax>
			<ymax>1527</ymax>
		</bndbox>
	</object>
	<object>
		<name>名称</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>1</difficult>
		<bndbox>
			<xmin>478</xmin>
			<ymin>355</ymin>
			<xmax>1482</xmax>
			<ymax>427</ymax>
		</bndbox>
	</object>
	<object>
		<name>纳税人识别号</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>1</difficult>
		<bndbox>
			<xmin>476</xmin>
			<ymin>425</ymin>
			<xmax>1484</xmax>
			<ymax>488</ymax>
		</bndbox>
	</object>
	<object>
		<name>地址电话</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>1</difficult>
		<bndbox>
			<xmin>476</xmin>
			<ymin>490</ymin>
			<xmax>1488</xmax>
			<ymax>546</ymax>
		</bndbox>
	</object>
	<object>
		<name>开户行及账号</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>1</difficult>
		<bndbox>
			<xmin>475</xmin>
			<ymin>542</ymin>
			<xmax>1488</xmax>
			<ymax>609</ymax>
		</bndbox>
	</object>
	<object>
		<name>货物或应税劳务、服务名称</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>1</difficult>
		<bndbox>
			<xmin>97</xmin>
			<ymin>661</ymin>
			<xmax>725</xmax>
			<ymax>807</ymax>
		</bndbox>
	</object>
	<object>
		<name>规格型号</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>1</difficult>
		<bndbox>
			<xmin>725</xmin>
			<ymin>657</ymin>
			<xmax>1032</xmax>
			<ymax>812</ymax>
		</bndbox>
	</object>
	<object>
		<name>单位</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>1</difficult>
		<bndbox>
			<xmin>1030</xmin>
			<ymin>655</ymin>
			<xmax>1206</xmax>
			<ymax>816</ymax>
		</bndbox>
	</object>
	<object>
		<name>数量</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>1</difficult>
		<bndbox>
			<xmin>1228</xmin>
			<ymin>668</ymin>
			<xmax>1460</xmax>
			<ymax>822</ymax>
		</bndbox>
	</object>
	<object>
		<name>单价</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>1</difficult>
		<bndbox>
			<xmin>1441</xmin>
			<ymin>668</ymin>
			<xmax>1710</xmax>
			<ymax>818</ymax>
		</bndbox>
	</object>
	<object>
		<name>金额</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>1</difficult>
		<bndbox>
			<xmin>1714</xmin>
			<ymin>668</ymin>
			<xmax>2049</xmax>
			<ymax>825</ymax>
		</bndbox>
	</object>
	<object>
		<name>税率</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>1</difficult>
		<bndbox>
			<xmin>2054</xmin>
			<ymin>661</ymin>
			<xmax>2204</xmax>
			<ymax>831</ymax>
		</bndbox>
	</object>
	<object>
		<name>税额</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>1</difficult>
		<bndbox>
			<xmin>2208</xmin>
			<ymin>664</ymin>
			<xmax>2512</xmax>
			<ymax>833</ymax>
		</bndbox>
	</object>
	<object>
		<name>合计</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>1</difficult>
		<bndbox>
			<xmin>1760</xmin>
			<ymin>1011</ymin>
			<xmax>2091</xmax>
			<ymax>1136</ymax>
		</bndbox>
	</object>
	<object>
		<name>税额</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>1</difficult>
		<bndbox>
			<xmin>2151</xmin>
			<ymin>985</ymin>
			<xmax>2497</xmax>
			<ymax>1133</ymax>
		</bndbox>
	</object>
	<object>
		<name>价税合计</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>1</difficult>
		<bndbox>
			<xmin>852</xmin>
			<ymin>1138</ymin>
			<xmax>1314</xmax>
			<ymax>1238</ymax>
		</bndbox>
	</object>
	<object>
		<name>价税合计</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>1</difficult>
		<bndbox>
			<xmin>1995</xmin>
			<ymin>1138</ymin>
			<xmax>2354</xmax>
			<ymax>1246</ymax>
		</bndbox>
	</object>
	<object>
		<name>销售方名称</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>1</difficult>
		<bndbox>
			<xmin>475</xmin>
			<ymin>1233</ymin>
			<xmax>1475</xmax>
			<ymax>1305</ymax>
		</bndbox>
	</object>
	<object>
		<name>销售方纳税人识别号</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>1</difficult>
		<bndbox>
			<xmin>469</xmin>
			<ymin>1294</ymin>
			<xmax>1486</xmax>
			<ymax>1362</ymax>
		</bndbox>
	</object>
	<object>
		<name>销售方地址电话</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>1</difficult>
		<bndbox>
			<xmin>473</xmin>
			<ymin>1351</ymin>
			<xmax>1482</xmax>
			<ymax>1418</ymax>
		</bndbox>
	</object>
	<object>
		<name>销售方开户行及账号</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>1</difficult>
		<bndbox>
			<xmin>473</xmin>
			<ymin>1401</ymin>
			<xmax>1488</xmax>
			<ymax>1474</ymax>
		</bndbox>
	</object>
	<object>
		<name>收款人</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>1</difficult>
		<bndbox>
			<xmin>319</xmin>
			<ymin>1466</ymin>
			<xmax>656</xmax>
			<ymax>1581</ymax>
		</bndbox>
	</object>
	<object>
		<name>复核</name>
		<pose>Unspecified</pose>
		<truncated>0</truncated>
		<difficult>1</difficult>
		<bndbox>
			<xmin>939</xmin>
			<ymin>1468</ymin>
			<xmax>1291</xmax>
			<ymax>1612</ymax>
		</bndbox>
	</object>
	<object>
		<name>开票人</name>
		<pose>Unspecified</pose>
		<truncated>1</truncated>
		<difficult>1</difficult>
		<bndbox>
			<xmin>1499</xmin>
			<ymin>1466</ymin>
			<xmax>1839</xmax>
			<ymax>1644</ymax>
		</bndbox>
	</object>
	<object>
		<name>销售方</name>
		<pose>Unspecified</pose>
		<truncated>1</truncated>
		<difficult>1</difficult>
		<bndbox>
			<xmin>2064</xmin>
			<ymin>1472</ymin>
			<xmax>2378</xmax>
			<ymax>1644</ymax>
		</bndbox>
	</object>
</annotation>
'''
    jsonstr ={
 "annotation": {
  "folder": "QQ",
  "filename": "model_yingye.jpg",
  "path": "E:\\QQ\\model_yingye.jpg",
  "source": {
   "database": "Unknown"
  },
  "size": {
   "width": "1080",
   "height": "1486",
   "depth": "3"
  },
  "segmented": "0",
  "object": [
   {
    "name": "\u6267\u7167",
    "pose": "Unspecified",
    "truncated": "0",
    "difficult": "0",
    "bndbox": {
     "xmin": "515",
     "ymin": "358",
     "xmax": "822",
     "ymax": "482"
    }
   },
   {
    "name": "\u540d\u79f0",
    "pose": "Unspecified",
    "truncated": "0",
    "difficult": "0",
    "bndbox": {
     "xmin": "146",
     "ymin": "623",
     "xmax": "328",
     "ymax": "673"
    }
   },
   {
    "name": "\u7c7b\u578b",
    "pose": "Unspecified",
    "truncated": "0",
    "difficult": "0",
    "bndbox": {
     "xmin": "140",
     "ymin": "668",
     "xmax": "333",
     "ymax": "718"
    }
   },
   {
    "name": "\u4f4f\u6240",
    "pose": "Unspecified",
    "truncated": "0",
    "difficult": "0",
    "bndbox": {
     "xmin": "136",
     "ymin": "705",
     "xmax": "330",
     "ymax": "753"
    }
   },
   {
    "name": "\u6cd5\u5b9a\u4ee3\u8868\u4eba",
    "pose": "Unspecified",
    "truncated": "0",
    "difficult": "0",
    "bndbox": {
     "xmin": "140",
     "ymin": "747",
     "xmax": "335",
     "ymax": "799"
    }
   },
   {
    "name": "\u6ce8\u518c\u8d44\u672c",
    "pose": "Unspecified",
    "truncated": "0",
    "difficult": "0",
    "bndbox": {
     "xmin": "136",
     "ymin": "787",
     "xmax": "336",
     "ymax": "837"
    }
   },
   {
    "name": "\u6210\u7acb\u65e5\u671f",
    "pose": "Unspecified",
    "truncated": "0",
    "difficult": "0",
    "bndbox": {
     "xmin": "131",
     "ymin": "826",
     "xmax": "336",
     "ymax": "882"
    }
   },
   {
    "name": "\u8425\u4e1a\u671f\u9650",
    "pose": "Unspecified",
    "truncated": "0",
    "difficult": "0",
    "bndbox": {
     "xmin": "130",
     "ymin": "871",
     "xmax": "333",
     "ymax": "918"
    }
   },
   {
    "name": "\u7ecf\u8425\u8303\u56f4",
    "pose": "Unspecified",
    "truncated": "0",
    "difficult": "0",
    "bndbox": {
     "xmin": "130",
     "ymin": "908",
     "xmax": "335",
     "ymax": "971"
    }
   },
   {
    "name": "\u540d\u79f0",
    "pose": "Unspecified",
    "truncated": "0",
    "difficult": "1",
    "bndbox": {
     "xmin": "331",
     "ymin": "621",
     "xmax": "741",
     "ymax": "679"
    }
   },
   {
    "name": "\u7c7b\u578b",
    "pose": "Unspecified",
    "truncated": "0",
    "difficult": "1",
    "bndbox": {
     "xmin": "334",
     "ymin": "670",
     "xmax": "758",
     "ymax": "715"
    }
   },
   {
    "name": "\u4f4f\u6240",
    "pose": "Unspecified",
    "truncated": "0",
    "difficult": "1",
    "bndbox": {
     "xmin": "325",
     "ymin": "712",
     "xmax": "767",
     "ymax": "758"
    }
   },
   {
    "name": "\u6cd5\u5b9a\u4ee3\u8868\u4eba",
    "pose": "Unspecified",
    "truncated": "0",
    "difficult": "1",
    "bndbox": {
     "xmin": "323",
     "ymin": "752",
     "xmax": "754",
     "ymax": "794"
    }
   },
   {
    "name": "\u6ce8\u518c\u8d44\u672c",
    "pose": "Unspecified",
    "truncated": "0",
    "difficult": "1",
    "bndbox": {
     "xmin": "330",
     "ymin": "791",
     "xmax": "609",
     "ymax": "839"
    }
   },
   {
    "name": "\u6210\u7acb\u65e5\u671f",
    "pose": "Unspecified",
    "truncated": "0",
    "difficult": "1",
    "bndbox": {
     "xmin": "322",
     "ymin": "834",
     "xmax": "610",
     "ymax": "878"
    }
   },
   {
    "name": "\u8425\u4e1a\u671f\u9650",
    "pose": "Unspecified",
    "truncated": "0",
    "difficult": "1",
    "bndbox": {
     "xmin": "328",
     "ymin": "876",
     "xmax": "752",
     "ymax": "923"
    }
   },
   {
    "name": "\u767b\u8bb0\u673a\u5173",
    "pose": "Unspecified",
    "truncated": "0",
    "difficult": "0",
    "bndbox": {
     "xmin": "490",
     "ymin": "1218",
     "xmax": "654",
     "ymax": "1263"
    }
   }
  ]
 }
}

    # jsontoxml(jsonstr)
    xmltojson(xml)

