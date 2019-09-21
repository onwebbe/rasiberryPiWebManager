from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def info(request):
  userInfo = {
    'id': '4291d7da9005377ec9aec4a71ea837f',
    'name': '天野远子',
    'username': 'admin',
    'password': '',
    'avatar': '/avatar2.jpg',
    'status': 1,
    'telephone': '',
    'lastLoginIp': '27.154.74.117',
    'lastLoginTime': 1534837621348,
    'creatorId': 'admin',
    'createTime': 1497160610259,
    'merchantCode': 'TLif2btpzg079h15bk',
    'deleted': 0,
    'roleId': 'admin',
    'role': {}
  }
  roleObj = {
    'permissions': [],
    'id': 'admin',
    'name': '管理员',
    'describe': '拥有所有权限',
    'status': 1,
    'creatorId': 'system',
    'createTime': 1497160610259,
    'deleted': 0,
    'permissions': [{
      'roleId': 'admin',
      'permissionId': 'dashboard',
      'permissionName': '仪表盘',
      'actions': '[{"action":"add","defaultCheck":false,"describe":"新增"},{"action":"query","defaultCheck":false,"describe":"查询"},{"action":"get","defaultCheck":false,"describe":"详情"},{"action":"update","defaultCheck":false,"describe":"修改"},{"action":"delete","defaultCheck":false,"describe":"删除"}]',
      'actionEntitySet': [{
        'action': 'add',
        'describe': '新增',
        'defaultCheck': False
      }, {
        'action': 'query',
        'describe': '查询',
        'defaultCheck': False
      }, {
        'action': 'get',
        'describe': '详情',
        'defaultCheck': False
      }, {
        'action': 'update',
        'describe': '修改',
        'defaultCheck': False
      }, {
        'action': 'delete',
        'describe': '删除',
        'defaultCheck': False
      }],
      'actionList': None,
      'dataAccess': None
    }, {
      'roleId': 'admin',
      'permissionId': 'exception',
      'permissionName': '异常页面权限',
      'actions': '[{"action":"add","defaultCheck":false,"describe":"新增"},{"action":"query","defaultCheck":false,"describe":"查询"},{"action":"get","defaultCheck":false,"describe":"详情"},{"action":"update","defaultCheck":false,"describe":"修改"},{"action":"delete","defaultCheck":false,"describe":"删除"}]',
      'actionEntitySet': [{
        'action': 'add',
        'describe': '新增',
        'defaultCheck': False
      }, {
        'action': 'query',
        'describe': '查询',
        'defaultCheck': False
      }, {
        'action': 'get',
        'describe': '详情',
        'defaultCheck': False
      }, {
        'action': 'update',
        'describe': '修改',
        'defaultCheck': False
      }, {
        'action': 'delete',
        'describe': '删除',
        'defaultCheck': False
      }],
      'actionList': None,
      'dataAccess': None
    }, {
      'roleId': 'admin',
      'permissionId': 'result',
      'permissionName': '结果权限',
      'actions': '[{"action":"add","defaultCheck":false,"describe":"新增"},{"action":"query","defaultCheck":false,"describe":"查询"},{"action":"get","defaultCheck":false,"describe":"详情"},{"action":"update","defaultCheck":false,"describe":"修改"},{"action":"delete","defaultCheck":false,"describe":"删除"}]',
      'actionEntitySet': [{
        'action': 'add',
        'describe': '新增',
        'defaultCheck': False
      }, {
        'action': 'query',
        'describe': '查询',
        'defaultCheck': False
      }, {
        'action': 'get',
        'describe': '详情',
        'defaultCheck': False
      }, {
        'action': 'update',
        'describe': '修改',
        'defaultCheck': False
      }, {
        'action': 'delete',
        'describe': '删除',
        'defaultCheck': False
      }],
      'actionList': None,
      'dataAccess': None
    }, {
      'roleId': 'admin',
      'permissionId': 'profile',
      'permissionName': '详细页权限',
      'actions': '[{"action":"add","defaultCheck":false,"describe":"新增"},{"action":"query","defaultCheck":false,"describe":"查询"},{"action":"get","defaultCheck":false,"describe":"详情"},{"action":"update","defaultCheck":false,"describe":"修改"},{"action":"delete","defaultCheck":false,"describe":"删除"}]',
      'actionEntitySet': [{
        'action': 'add',
        'describe': '新增',
        'defaultCheck': False
      }, {
        'action': 'query',
        'describe': '查询',
        'defaultCheck': False
      }, {
        'action': 'get',
        'describe': '详情',
        'defaultCheck': False
      }, {
        'action': 'update',
        'describe': '修改',
        'defaultCheck': False
      }, {
        'action': 'delete',
        'describe': '删除',
        'defaultCheck': False
      }],
      'actionList': None,
      'dataAccess': None
    }, {
      'roleId': 'admin',
      'permissionId': 'table',
      'permissionName': '表格权限',
      'actions': '[{"action":"add","defaultCheck":false,"describe":"新增"},{"action":"import","defaultCheck":false,"describe":"导入"},{"action":"get","defaultCheck":false,"describe":"详情"},{"action":"update","defaultCheck":false,"describe":"修改"}]',
      'actionEntitySet': [{
        'action': 'add',
        'describe': '新增',
        'defaultCheck': False
      }, {
        'action': 'import',
        'describe': '导入',
        'defaultCheck': False
      }, {
        'action': 'get',
        'describe': '详情',
        'defaultCheck': False
      }, {
        'action': 'update',
        'describe': '修改',
        'defaultCheck': False
      }],
      'actionList': None,
      'dataAccess': None
    }, {
      'roleId': 'admin',
      'permissionId': 'form',
      'permissionName': '表单权限',
      'actions': '[{"action":"add","defaultCheck":false,"describe":"新增"},{"action":"get","defaultCheck":false,"describe":"详情"},{"action":"query","defaultCheck":false,"describe":"查询"},{"action":"update","defaultCheck":false,"describe":"修改"},{"action":"delete","defaultCheck":false,"describe":"删除"}]',
      'actionEntitySet': [{
        'action': 'add',
        'describe': '新增',
        'defaultCheck': False
      }, {
        'action': 'get',
        'describe': '详情',
        'defaultCheck': False
      }, {
        'action': 'query',
        'describe': '查询',
        'defaultCheck': False
      }, {
        'action': 'update',
        'describe': '修改',
        'defaultCheck': False
      }, {
        'action': 'delete',
        'describe': '删除',
        'defaultCheck': False
      }],
      'actionList': None,
      'dataAccess': None
    }, {
      'roleId': 'admin',
      'permissionId': 'order',
      'permissionName': '订单管理',
      'actions': '[{"action":"add","defaultCheck":false,"describe":"新增"},{"action":"query","defaultCheck":false,"describe":"查询"},{"action":"get","defaultCheck":false,"describe":"详情"},{"action":"update","defaultCheck":false,"describe":"修改"},{"action":"delete","defaultCheck":false,"describe":"删除"}]',
      'actionEntitySet': [{
        'action': 'add',
        'describe': '新增',
        'defaultCheck': False
      }, {
        'action': 'query',
        'describe': '查询',
        'defaultCheck': False
      }, {
        'action': 'get',
        'describe': '详情',
        'defaultCheck': False
      }, {
        'action': 'update',
        'describe': '修改',
        'defaultCheck': False
      }, {
        'action': 'delete',
        'describe': '删除',
        'defaultCheck': False
      }],
      'actionList': None,
      'dataAccess': None
    }, {
      'roleId': 'admin',
      'permissionId': 'permission',
      'permissionName': '权限管理',
      'actions': '[{"action":"add","defaultCheck":false,"describe":"新增"},{"action":"get","defaultCheck":false,"describe":"详情"},{"action":"update","defaultCheck":false,"describe":"修改"},{"action":"delete","defaultCheck":false,"describe":"删除"}]',
      'actionEntitySet': [{
        'action': 'add',
        'describe': '新增',
        'defaultCheck': False
      }, {
        'action': 'get',
        'describe': '详情',
        'defaultCheck': False
      }, {
        'action': 'update',
        'describe': '修改',
        'defaultCheck': False
      }, {
        'action': 'delete',
        'describe': '删除',
        'defaultCheck': False
      }],
      'actionList': None,
      'dataAccess': None
    }, {
      'roleId': 'admin',
      'permissionId': 'role',
      'permissionName': '角色管理',
      'actions': '[{"action":"add","defaultCheck":false,"describe":"新增"},{"action":"get","defaultCheck":false,"describe":"详情"},{"action":"update","defaultCheck":false,"describe":"修改"},{"action":"delete","defaultCheck":false,"describe":"删除"}]',
      'actionEntitySet': [{
        'action': 'add',
        'describe': '新增',
        'defaultCheck': False
      }, {
        'action': 'get',
        'describe': '详情',
        'defaultCheck': False
      }, {
        'action': 'update',
        'describe': '修改',
        'defaultCheck': False
      }, {
        'action': 'delete',
        'describe': '删除',
        'defaultCheck': False
      }],
      'actionList': None,
      'dataAccess': None
    }, {
      'roleId': 'admin',
      'permissionId': 'table',
      'permissionName': '桌子管理',
      'actions': '[{"action":"add","defaultCheck":false,"describe":"新增"},{"action":"get","defaultCheck":false,"describe":"详情"},{"action":"query","defaultCheck":false,"describe":"查询"},{"action":"update","defaultCheck":false,"describe":"修改"},{"action":"delete","defaultCheck":false,"describe":"删除"}]',
      'actionEntitySet': [{
        'action': 'add',
        'describe': '新增',
        'defaultCheck': False
      }, {
        'action': 'get',
        'describe': '详情',
        'defaultCheck': False
      }, {
        'action': 'query',
        'describe': '查询',
        'defaultCheck': False
      }, {
        'action': 'update',
        'describe': '修改',
        'defaultCheck': False
      }, {
        'action': 'delete',
        'describe': '删除',
        'defaultCheck': False
      }],
      'actionList': None,
      'dataAccess': None
    }, {
      'roleId': 'admin',
      'permissionId': 'user',
      'permissionName': '用户管理',
      'actions': '[{"action":"add","defaultCheck":false,"describe":"新增"},{"action":"import","defaultCheck":false,"describe":"导入"},{"action":"get","defaultCheck":false,"describe":"详情"},{"action":"update","defaultCheck":false,"describe":"修改"},{"action":"delete","defaultCheck":false,"describe":"删除"},{"action":"export","defaultCheck":false,"describe":"导出"}]',
      'actionEntitySet': [{
        'action': 'add',
        'describe': '新增',
        'defaultCheck': False
      }, {
        'action': 'import',
        'describe': '导入',
        'defaultCheck': False
      }, {
        'action': 'get',
        'describe': '详情',
        'defaultCheck': False
      }, {
        'action': 'update',
        'describe': '修改',
        'defaultCheck': False
      }, {
        'action': 'delete',
        'describe': '删除',
        'defaultCheck': False
      }, {
        'action': 'export',
        'describe': '导出',
        'defaultCheck': False
      }],
      'actionList': None,
      'dataAccess': None
    }],
    'permissions': [{
      'roleId': 'admin',
      'permissionId': 'support',
      'permissionName': '超级模块',
      'actions': '[{"action":"add","defaultCheck":false,"describe":"新增"},{"action":"import","defaultCheck":false,"describe":"导入"},{"action":"get","defaultCheck":false,"describe":"详情"},{"action":"update","defaultCheck":false,"describe":"修改"},{"action":"delete","defaultCheck":false,"describe":"删除"},{"action":"export","defaultCheck":false,"describe":"导出"}]',
      'actionEntitySet': [{
        'action': 'add',
        'describe': '新增',
        'defaultCheck': False
      }, {
        'action': 'import',
        'describe': '导入',
        'defaultCheck': False
      }, {
        'action': 'get',
        'describe': '详情',
        'defaultCheck': False
      }, {
        'action': 'update',
        'describe': '修改',
        'defaultCheck': False
      }, {
        'action': 'delete',
        'describe': '删除',
        'defaultCheck': False
      }, {
        'action': 'export',
        'describe': '导出',
        'defaultCheck': False
      }],
      'actionList': None,
      'dataAccess': None
    }, {
      'roleId': 'admin',
      'permissionId': 'pioverview',
      'permissionName': 'pioverview',
      'actions': '[{"action":"add","defaultCheck":false,"describe":"新增"},{"action":"query","defaultCheck":false,"describe":"查询"},{"action":"get","defaultCheck":false,"describe":"详情"},{"action":"update","defaultCheck":false,"describe":"修改"},{"action":"delete","defaultCheck":false,"describe":"删除"}]',
      'actionEntitySet': [{
        'action': 'add',
        'describe': '新增',
        'defaultCheck': False
      }, {
        'action': 'query',
        'describe': '查询',
        'defaultCheck': False
      }, {
        'action': 'get',
        'describe': '详情',
        'defaultCheck': False
      }, {
        'action': 'update',
        'describe': '修改',
        'defaultCheck': False
      }, {
        'action': 'delete',
        'describe': '删除',
        'defaultCheck': False
      }],
      'actionList': None,
      'dataAccess': None
    }]
  }

  userInfo = {
    'result': {
      'role': roleObj
    }
  }
  return HttpResponse(json.dumps(userInfo, indent=4))

def nav(request):
  nav = [
    # // dashboard
    {
      'name': 'dashboard',
      'parentId': -1,
      'id': 1,
      'meta': {
        'icon': 'dashboard',
        'title': '仪表盘',
        'show': True
      },
      'component': 'RouteView',
      'redirect': '/dashboard/workplace'
    },
    {
      'name': 'workplace',
      'parentId': 1,
      'id': 7,
      'meta': {
        'title': '工作台',
        'show': True
      },
      'component': 'Workplace'
    },
    {
      'name': 'monitor',
      'path': 'https://www.baidu.com/',
      'parentId': 1,
      'id': 3,
      'meta': {
        'title': '监控页（外部）',
        'target': '_blank',
        'show': True
      }
    },
    {
      'name': 'analysis',
      'parentId': 1,
      'id': 2,
      'meta': {
        'title': '分析页',
        'show': True
      },
      'component': 'Analysis'
    },
    {
      'name': 'tests',
      'parentId': 1,
      'id': 8,
      'meta': {
        'title': '测试功能',
        'show': True
      },
      'component': 'TestWork'
    },

    # //pi overview
    {
      'name': 'pioverview',
      'parentId': -1,
      'id': 100,
      'meta': {
        'icon': 'dashboard',
        'title': 'Pi Overview',
        'show': True
      },
      'component': 'RouteView',
      'redirect': '/pioverview/gpioOverview'
    },
    {
      'name': 'gpioOverview',
      'parentId': 100,
      'id': 6,
      'meta': {
        'title': 'GPIO Overview'
      },
      'component': 'PiGPIOStatus'
    },
    {
      'name': 'workingOverview',
      'parentId': 100,
      'id': 7,
      'meta': {
        'title': 'Woring Overview'
      },
      'component': 'PiWorkingStatus'
    },
    # // form
    {
      'name': 'form',
      'parentId': -1,
      'id': 10,
      'meta': {
        'icon': 'form',
        'title': '表单页'
      },
      'redirect': '/form/base-form',
      'component': 'PageView'
    },
    {
      'name': 'basic-form',
      'parentId': 10,
      'id': 6,
      'meta': {
        'title': '基础表单'
      },
      'component': 'BasicForm'
    },
    {
      'name': 'step-form',
      'parentId': 10,
      'id': 5,
      'meta': {
        'title': '分步表单'
      },
      'component': 'StepForm'
    },
    {
      'name': 'advanced-form',
      'parentId': 10,
      'id': 4,
      'meta': {
        'title': '高级表单'
      },
      'component': 'AdvanceForm'
    },

    # // list
    {
      'name': 'list',
      'parentId': -1,
      'id': 10010,
      'meta': {
        'icon': 'table',
        'title': '列表页',
        'show': True
      },
      'redirect': '/list/table-list',
      'component': 'PageView'
    },
    {
      'name': 'table-list',
      'parentId': 10010,
      'id': 10011,
      'path': '/list/table-list/:pageNo([1-9]\\d*)?',
      'meta': {
        'title': '查询表格',
        'show': True
      },
      'component': 'TableList'
    },
    {
      'name': 'basic-list',
      'parentId': 10010,
      'id': 10012,
      'meta': {
        'title': '标准列表',
        'show': True
      },
      'component': 'StandardList'
    },
    {
      'name': 'card',
      'parentId': 10010,
      'id': 10013,
      'meta': {
        'title': '卡片列表',
        'show': True
      },
      'component': 'CardList'
    },
    {
      'name': 'search',
      'parentId': 10010,
      'id': 10014,
      'meta': {
        'title': '搜索列表',
        'show': True
      },
      'redirect': '/list/search/article',
      'component': 'SearchLayout'
    },
    {
      'name': 'article',
      'parentId': 10014,
      'id': 10015,
      'meta': {
        'title': '搜索列表（文章）',
        'show': True
      },
      'component': 'SearchArticles'
    },
    {
      'name': 'project',
      'parentId': 10014,
      'id': 10016,
      'meta': {
        'title': '搜索列表（项目）',
        'show': True
      },
      'component': 'SearchProjects'
    },
    {
      'name': 'application',
      'parentId': 10014,
      'id': 10017,
      'meta': {
        'title': '搜索列表（应用）',
        'show': True
      },
      'component': 'SearchApplications'
    },

    # // profile
    {
      'name': 'profile',
      'parentId': -1,
      'id': 10018,
      'meta': {
        'title': '详情页',
        'icon': 'profile',
        'show': True
      },
      'redirect': '/profile/basic',
      'component': 'RouteView'
    },
    {
      'name': 'basic',
      'parentId': 10018,
      'id': 10019,
      'meta': {
        'title': '基础详情页',
        'show': True
      },
      'component': 'ProfileBasic'
    },
    {
      'name': 'advanced',
      'parentId': 10018,
      'id': 10020,
      'meta': {
        'title': '高级详情页',
        'show': True
      },
      'component': 'ProfileAdvanced'
    },

    # // result
    {
      'name': 'result',
      'parentId': -1,
      'id': 10021,
      'meta': {
        'title': '结果页',
        'icon': 'check-circle-o',
        'show': True
      },
      'redirect': '/result/success',
      'component': 'PageView'
    },
    {
      'name': 'success',
      'parentId': 10021,
      'id': 10022,
      'meta': {
        'title': '成功',
        'hiddenHeaderContent': True,
        'show': True
      },
      'component': 'ResultSuccess'
    },
    {
      'name': 'fail',
      'parentId': 10021,
      'id': 10023,
      'meta': {
        'title': '失败',
        'hiddenHeaderContent': True,
        'show': True
      },
      'component': 'ResultFail'
    },

    # // Exception
    {
      'name': 'exception',
      'parentId': -1,
      'id': 10024,
      'meta': {
        'title': '异常页',
        'icon': 'warning',
        'show': True
      },
      'redirect': '/exception/403',
      'component': 'RouteView'
    },
    {
      'name': '403',
      'parentId': 10024,
      'id': 10025,
      'meta': {
        'title': '403',
        'show': True
      },
      'component': 'Exception403'
    },
    {
      'name': '404',
      'parentId': 10024,
      'id': 10026,
      'meta': {
        'title': '404',
        'show': True
      },
      'component': 'Exception404'
    },
    {
      'name': '500',
      'parentId': 10024,
      'id': 10027,
      'meta': {
        'title': '500',
        'show': True
      },
      'component': 'Exception500'
    },

    # // account
    {
      'name': 'account',
      'parentId': -1,
      'id': 10028,
      'meta': {
        'title': '个人页',
        'icon': 'user',
        'show': True
      },
      'redirect': '/account/center',
      'component': 'RouteView'
    },
    {
      'name': 'center',
      'parentId': 10028,
      'id': 10029,
      'meta': {
        'title': '个人中心',
        'show': True
      },
      'component': 'AccountCenter'
    },
    # // 特殊三级菜单
    {
      'name': 'settings',
      'parentId': 10028,
      'id': 10030,
      'meta': {
        'title': '个人设置',
        'hideHeader': True,
        'hideChildren': True,
        'show': True
      },
      'redirect': '/account/settings/base',
      'component': 'AccountSettings'
    },
    {
      'name': 'BaseSettings',
      'path': '/account/settings/base',
      'parentId': 10030,
      'id': 10031,
      'meta': {
        'title': '基本设置',
        'show': False
      },
      'component': 'BaseSettings'
    },
    {
      'name': 'SecuritySettings',
      'path': '/account/settings/security',
      'parentId': 10030,
      'id': 10032,
      'meta': {
        'title': '安全设置',
        'show': False
      },
      'component': 'SecuritySettings'
    },
    {
      'name': 'CustomSettings',
      'path': '/account/settings/custom',
      'parentId': 10030,
      'id': 10033,
      'meta': {
        'title': '个性化设置',
        'show': False
      },
      'component': 'CustomSettings'
    },
    {
      'name': 'BindingSettings',
      'path': '/account/settings/binding',
      'parentId': 10030,
      'id': 10034,
      'meta': {
        'title': '账户绑定',
        'show': False
      },
      'component': 'BindingSettings'
    },
    {
      'name': 'NotificationSettings',
      'path': '/account/settings/notification',
      'parentId': 10030,
      'id': 10034,
      'meta': {
        'title': '新消息通知',
        'show': False
      },
      'component': 'NotificationSettings'
    }
  ]
  navResult = {
    'result': nav
  }
  return HttpResponse(json.dumps(navResult, indent=4))
