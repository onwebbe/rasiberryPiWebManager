import BasicLayout from '@/layouts/BasicLayout';
import Dashboard from '@/pages/Dashboard';
import NotFound from '@/pages/NotFound';
import GpioPinOverall from '@/pages/GpioPinOverall';

const routerConfig = [
  {
    path: '/',
    component: BasicLayout,
    children: [
      { path: '/dashboard', component: Dashboard },
      { path: '/gpio/pinoverall', component: GpioPinOverall },
      { path: '/', redirect: '/dashboard' },
      { component: NotFound },
    ],
  },
];

export default routerConfig;
