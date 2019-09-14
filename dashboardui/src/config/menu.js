// 菜单配置
// headerMenuConfig：头部导航配置
// asideMenuConfig：侧边导航配置

const headerMenuConfig = [
  {
    name: '反馈',
    path: 'https://github.com/alibaba/ice',
    external: true,
    newWindow: true,
    icon: 'email',
  },

  {
    name: '帮助',
    path: 'https://alibaba.github.io/ice',
    external: true,
    newWindow: true,
    icon: 'help',
  },
];

const asideMenuConfig = [
  {
    name: 'Dashboard',
    path: '/dashboard',
    icon: 'atm',
    children: [
      {
        name: '监控页',
        path: '/dashboard/monitor',
        id: 'Menu_rnd3m',
        children: [
          { name: '通用图表', path: '/chart/general', id: 'Menu_a0xhu' },
          { name: '基础图表', path: '/chart/basic', id: 'Menu_4jrqn' },
        ],
      },
    ],
    id: 'Menu_d7py2',
  },
  {
    name: 'GPIO操作',
    path: '/chart',
    icon: 'picture',
    children: [
      { name: 'GPIOPinOverall', path: '/gpio/pinoverall', id: 'Menu_dxhct' },
    ],
    id: 'Menu_fvy2p',
  },
  {
    name: '表格页',
    path: '/table',
    icon: 'calendar',
    children: [
      { name: '基础表格', path: '/table/basic', id: 'Menu_d301s' },
      { name: '通用表格', path: '/table/general', id: 'Menu_94obq' },
    ],
    id: 'Menu_k6ivq',
  },
];

export { headerMenuConfig, asideMenuConfig };
