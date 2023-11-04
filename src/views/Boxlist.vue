<template>
    <div class="container mx-auto mt-8">
      <div class="flex flex-wrap justify-center -mx-4">
        <div class="w-full sm:w-1/2 md:w-1/3 px-4 mb-4" v-for="(item, index) in items" :key="index">
          <div class="bg-white shadow-lg p-4 rounded-lg w-72 h-72 m-4 mx-auto relative">
            <!-- เพิ่มรูปภาพและกำหนดให้อยู่ตรงกลาง -->
            <img
              
              alt="Box image" 
              class="mx-auto absolute top-0 left-0 right-0 bottom-0"
              style="max-height: 50%; max-width: 50%; margin: auto;"
            >
            <h2 class="text-xl font-semibold mb-2">ข้อมูลที่ {{ item }}</h2>
            <p>ข้อมูลเกี่ยวกับรายการที่ {{ item }} อยู่ที่นี่...</p>
          </div>
          <div class="text-center mt-2 relative">
            <div style="display: inline;">เพิ่มเส้นใต้นะ</div> 
          </div>
          <div class="w-full text-center mt-2">
            <div class="w-2/3 h-1 bg-black mx-auto" style="margin-top: 2px;"></div>
          </div>
          <!-- เริ่มบรรทัดใหม่ทุก 3 กล่อง -->
          <div v-if="(index + 1) % 3 === 0" class="w-full"></div>
        </div>
      </div>
    </div>

    <label class="max-w-[200px] text-center mt-2">ow</label> 
          <input type="number" :value="OW" readonly class="border border-gray-300 p-2 rounded mt-2"> 

          <label class="max-w-[200px] text-center mt-2">ow</label> 
          <input type="number" :value="IW" readonly class="border border-gray-300 p-2 rounded mt-2"> 
  </template>

  
  <script> 
  export default {
    name: "Boxlist-t",
    data() {
      return {
        items: [1, 2, 3, 4, 5, 6], // แก้ไขรายการตามที่คุณต้องการ
      };
    },
    computed: {
     OW() {
      return this.$store.getters.getFormOutput.OW;

    },
     IW() {
       return this.$store.getters.getFormOutput.IW;
    },

    },
  };
  </script>