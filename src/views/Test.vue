<template>
  <div class="mt-8 flex items-center justify-center">
    <img :src="imageUrl" alt="Centered Image" class="w-50 h-50">
  </div>

  <div class="flex flex-col items-center justify-center h-screen bg-gray-100">
    <button @click="onConfirm" class="mt-4 bg-blue-500 text-white px-4 py-2 rounded">
      ยืนยัน
    </button>
    <label class="max-w-[200px] text-center mt-2">
      ลังมีไส้หรือไม่
      <span class="ml-2">
        <input type="radio" v-model="withFilling" value="1" disabled>มี
      </span>
      <span class="ml-2">
        <input type ="radio" v-model="withFilling" value="0" disabled>ไม่มี
      </span>
    </label>

    <label class="max-w-[200px] text-center mt-2">ประเภทของแผ่นมาตรฐาน</label>
    <input type="text" :value="inputType" readonly class="border border-gray-300 p-2 rounded mt-2">

    <div class="grid grid-cols-2 gap-4">
      <div class="flex flex-col">
        <label class="max-w-[200px] text-center mt-2">ความกว้างลัง</label>
        <input type="number" :value="inputWidth" readonly class="border border-gray-300 p-2 rounded mt-2">

        <label class="max-w-[200px] text-center mt-2">ความยาวลัง</label>
        <input type="number" :value="inputLength" readonly class="border border-gray-300 p-2 rounded mt-2">

        <label class="max-w-[200px] text-center mt-2">ความสูงลัง</label>
        <input type="number" :value="inputHeight" readonly class="border border-gray-300 p-2 rounded mt-2">

        <label class="max-w-[200px] text-center mt-2">ความหนาลัง</label>
        <input type="number" :value="inputThick" readonly class="border border-gray-300 p-2 rounded mt-2">

        <label class="max-w-[200px] text-center mt-2">ชุดไส้มีผนังร่วมหรือไม่</label>
        <input type="text" :value="inputSkin" readonly class="border border-gray-300 p-2 rounded mt-2">
      </div>

      <div class="flex flex-col">
        <label class="max-w-[200px] text-center mt-2">จำนวนช่องเเบ่งด้านกว้าง</label>
        <input type="number" :value="withFilling === 'no' ? '-' : spaceofwidth" readonly class="border border-gray-300 p-2 rounded mt-2">

        <label class="max-w-[200px] text-center mt-2">จำนวนช่องเเบ่งด้านยาว</label>
        <input type="number" :value="withFilling === 'no' ? '-' : spaceoflength" readonly class="border border-gray-300 p-2 rounded mt-2">

        <label class="max-w-[200px] text-center mt-2">ค่าความหนาของเเผ่นคั่น</label>
        <input type="number" :value="withFilling === 'no' ? '-' : thickness" readonly class="border border-gray-300 p-2 rounded mt-2">

        <label class="max-w-[200px] text-center mt-2">ค่าความบวกเพิ่่มของเเผ่นคั่น</label>
        <input type="number" :value="withFilling === 'no' ? '-' : additional" readonly class="border border-gray-300 p-2 rounded mt-2">
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "Test-T",
  data() {
    return {
      imageUrl: 'https://via.placeholder.com/250',
    };
  },
  computed: {
    inputWidth() {
      return this.$store.getters.getFormData.width;
    },
    inputLength() {
      return this.$store.getters.getFormData.length;
    },
    inputHeight() {
      return this.$store.getters.getFormData.height;
    },
    inputThick() {
      return this.$store.getters.getFormData.thick;
    },
    inputType() {
      return this.$store.getters.getFormData.type;
    },
    withFilling() {
      return this.$store.getters.getFormData.hasIt;
    },
    inputSkin() {
      return this.$store.getters.getFormData.hasskin;
    },
    spaceofwidth() {
      return this.$store.getters.getFormData.amountofwidth;
    },
    spaceoflength() {
      return this.$store.getters.getFormData.amountoflength;
    },
    thickness() {
      return this.$store.getters.getFormData.thickness;
    },
    additional() {
      return this.$store.getters.getFormData.additional;
    },
  },
  methods: {
    onToHome() {
      this.$router.push('/');
    },
    async onConfirm() {
      const dataToSend = {
        width: this.inputWidth,
        length: this.inputLength,
        height: this.inputHeight,
        thick: this.inputThick,
        type: this.inputType,
        hasIt: this.withFilling,
        hasskin: this.inputSkin,
        amountofwidth: this.spaceofwidth,
        amountoflength: this.spaceoflength,
        thickness: this.thickness,
        additional: this.additional,
        // Add other properties as needed
      };

      const backendURL = 'http://localhost:8000/submit-form';
      console.log('ยืนยัน', 'ความกว้าง:', this.inputWidth, 'ความยาว:', this.inputLength, 'ความสูง:', this.inputHeight, 'ประเภท:', this.inputType, 'ลังมีไส้:', this.withFilling);
      var _temp = JSON.parse(JSON.stringify(dataToSend))
      _temp.hasIt = _temp.hasIt === "1" ? true : false;

      axios.post(backendURL, _temp)
        .then(response => {
          console.log('รับข้อมูลจาก backend:', response.data);
          this.$store.dispatch("setOutput", {
            OW: response.data.OW,
            IW: response.data.IW,
            FL: response.data.FL,
            PL: response.data.PL,
            OO: response.data.OO,
            II: response.data.II,
            OP: response.data.OP,
            IP: response.data.IP,
            PW: response.data.PW,
            x: response.data.x,
            AW1: response.data.AW1, // Add AW1
            AW2: response.data.AW2, // Add AW2
          });
          // Do what you need to do after receiving the response from the backend
          this.$router.push('/t3');
        })
        .catch(error => {
          console.error('เกิดข้อผิดพลาดในการส่งข้อมูลไปยัง backend:', error);
          // Handle errors that occur
        });
    },
  },
};
</script>

<style scoped>
/* Styles for the component */
/* Add your styles for the component here */
</style>
