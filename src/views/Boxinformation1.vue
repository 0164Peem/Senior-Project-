<template>
  <div class="mt-8 flex items-center justify-center">
    <img :src="imageUrl" alt="Centered Image" class="w-50 h-50">
  </div>

  <div class="flex flex-col items-center justify-center h-screen bg-gray-100">
    <button @click="onConfirm" class="mt-4 bg-blue-500 text-white px-4 py-2 rounded">
      ยืนยัน
    </button>
    <label class="max-w-[200px] text-center mt-2">
      <!-- Your radio buttons here -->
    </label>
    <label class="max-w-[200px] text-center mt-2">
      ประเภทของแผ่นมาตรฐาน
      <input type="text" :value="inputType" readonly class="border border-gray-300 p-2 rounded mt-2">
    </label>

    <div class="grid grid-cols-3 gap-4">
      <!-- First Column -->
      <div class="flex flex-col">
        <label class="max-w-[200px] text-center mt-2">ความกว้างเเผ่นต่อ</label>
        <input type="number" :value="AW1" readonly class="border border-gray-300 p-2 rounded mt-2">
        <label class="max-w-[200px] text-center mt-2">ความสูงเเผ่นต่อ</label>
        <input type="number" :value="AH1" readonly class="border border-gray-300 p-2 rounded mt-2">

        <label class="max-w-[200px] text-center mt-2" style="display: inline; white-space: nowrap;">ความกว้างแผ่นต่อของลัง45องศา</label>


        <input type="number" :value="AW2" readonly class="border border-gray-300 p-2 rounded mt-2">

        <label class="max-w-[200px] text-center mt-2">ความสูงแผ่นต่อของลัง45องศา</label> 
        <input type="number" :value="AH2" readonly class="border border-gray-300 p-2 rounded mt-2">


        <label class="max-w-[200px] text-center mt-2">ความยาวของด้านกว้างแผ่นเตรียมก่อนตัด+เผื่อปั้ม </label> 
        <input type="number" :value="PW" readonly class="border border-gray-300 p-2 rounded mt-2">



        
      </div>

      <!-- Second Column -->
      <div class="flex flex-col">
        <label class="max-w-[200px] text-center mt-2">ความกว้างเเบบกาง(นอก)</label>
        <input type="number" :value="OW" readonly class="border border-gray-300 p-2 rounded mt-2">
        <label class="max-w-[200px] text-center mt-2">ความกว้างเเบบกาง(ใน)</label>
        <input type="number" :value="IW" readonly class="border border-gray-300 p-2 rounded mt-2">

         <label class="max-w-[200px] text-center mt-2">เผื่อพับเเบบกาง(นอก)</label>
        <input type="number" :value="OO" readonly class="border border-gray-300 p-2 rounded mt-2">

        <label class="max-w-[200px] text-center mt-2">เผื่อพับเเบบกาง(ใน)</label>
        <input type="number" :value="II" readonly class="border border-gray-300 p-2 rounded mt-2">

        <label class="max-w-[200px] text-center mt-2">ความยาวของด้านยาวแผ่นเตรียมก่อนตัด+เผื่อปั้ม</label> 
        <input type="number" :value="PL" readonly class="border border-gray-300 p-2 rounded mt-2">
      </div>

      <!-- Third Column -->
      <div class="flex flex-col">
         <label class="max-w-[200px] text-center mt-2" style="display: inline; white-space: nowrap;">ความยาวของปีกพับความสูง(ใน)</label>
        <input type="number" :value="OP" readonly class="border border-gray-300 p-2 rounded mt-2">
        <label class="max-w-[200px] text-center mt-2" style="display: inline; white-space: nowrap;">ความยาวของปีกพักความกว้าง(นอก)</label> 
        <input type="number" :value="IP" readonly class="border border-gray-300 p-2 rounded mt-2">

         <label class="max-w-[200px] text-center mt-2" style="display: inline; white-space: nowrap;">ความยาวของด้านกว้างแผ่นเตรียมก่อนตัด</label>
        <input type="number" :value="FW" readonly class="border border-gray-300 p-2 rounded mt-2">

        <label class="max-w-[200px]  text-center mt-2" style="display: inline; white-space: nowrap;">ความยาวของด้านยาวแผ่นเตรียมก่อนตัด</label>
        <input type="number" :value="FL" readonly class="border border-gray-300 p-2 rounded mt-2">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Boxinformation-t",
  data() {
    return {
      imageUrl: 'https://via.placeholder.com/250',
    };
  },
  computed: {
    OW() {
      return this.$store.getters.getFormOutput.OW;
    },
    IW() {
      return this.$store.getters.getFormOutput.IW;
    },
     FL() {
    return this.$store.getters.getFormOutput.FL;
  },
  PL() {
    return this.$store.getters.getFormOutput.PL;
  },
  OO() {
    return this.$store.getters.getFormOutput.OO;
  },
  II() {
    return this.$store.getters.getFormOutput.II;
  },
  OP() {
    return this.$store.getters.getFormOutput.OP;
  },
  IP() {
    return this.$store.getters.getFormOutput.IP;
  },
  PW() {
    return this.$store.getters.getFormOutput.PW;
  },
  AW1() {
    return this.$store.getters.getFormOutput.AW1;
  },
  AW2() {
    return this.$store.getters.getFormOutput.AW2;
  }
  }
};
</script>

<style>
  /* Add your styles here */
</style>
