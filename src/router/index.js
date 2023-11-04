
import {createRouter,createWebHistory} from 'vue-router';
import home from '@/views/InputForm.vue';
import p2 from '@/views/Test.vue';
import p4 from  '@/views/Boxlist.vue';
import p3 from  '@/views/Boxinformation1.vue';

const routes =[    
        { path: '/', component: home  },          
        { path: '/t2', component: p2  },   
        { path: '/t3', component: p3  },  
        { path: '/t4', component: p4  },  
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
  });
  
  export default router;