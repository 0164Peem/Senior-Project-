<template>
  <!-- <div class="flex"> -->
    <!-- Left Section -->
    <div class=" p-8 flex flex-col justify-center">
      <h2 class="text-2xl font-semibold mb-4 text-center">กรอกข้อมูล</h2>
      <form class="w-full" v-on:submit.prevent="submitForm" >
        <div class="custom-layout">
          <div></div>
          <div class="layout-main">
            <div class="mb-4 flex flex-row items-center">
              <label for="name" class="block text-gray-600 w-1/4 " 
                >ใส่ความกว้างลัง(ซม.):</label
              >
              <input
                type="text"
                id="name1"
                name="name1"
                class="border rounded px-4 py-2 w-3/4"
                placeholder="ใส่ความกว้างของลัง"
                v-model="formData.width"
                required 
              />
            </div>
            <div class="mb-4 flex flex-row items-center">
              <label for="name" class="block text-gray-600 w-1/4"
                >ใส่ความยาวลัง(ซม.):</label
              >
              <input
                type="text"
                id="name2"
                name="name2"
                class="border rounded px-4 py-2 w-3/4"
                placeholder="ใส่ความยาวของลัง"
                v-model="formData.length"
                required 
              />
            </div>
            <div class="mb-4 flex flex-row items-center">
              <label for="name" class="block text-gray-600 w-1/4"
                >ใส่ความสูงลัง(ซม.):</label
              >
              <input
                type="text"
                id="name3"
                name="name3"
                class="border rounded px-4 py-2 w-3/4"
                v-model="formData.height"
                placeholder="ใส่ความสูงลัง"
                required 
              />
            </div>
            <div class="mb-4 flex flex-row items-center">
              <label for="name" class="block text-gray-600 w-1/4"
                >ใส่ความหนาของเเผ่นมาตราฐาน(มม.):</label 
              >
              <input
                type="text"
                id="name4"
                name="name4"
                class="border rounded px-4 py-2 w-3/4"
                v-model="formData.thick"
                placeholder="ใส่ความหนาของเเผ่นมาตราฐาน"
                required 
              />
            </div>
            <div class="mb-4 flex flex-row items-center">
              <label for="standard_type" class="block text-gray-600 w-1/4"
                >เลือกประเภทของแผ่นมาตรฐาน:</label
              >
              <select
                id="standard_type"
                name="standard_type"
                class="border rounded px-4 py-2 w-3/4"
                v-model="formData.type"
                required 
                
              >
               <option value="" disabled selected>เลือกประเภท</option>
                <option value="65x150">65x150</option>
                <option value="65x245">65x245</option>
                <option value="130x150">130x150</option>
                <option value="150x180">150x180</option>
                 <option value="150x245">150x245</option> 
              </select>
            </div>
            <div class="mb-4 flex flex-row items-center">
              <label for="name" class="block text-gray-600 w-1/4"
                >ใส่ค่าบวกเพิ่มแผ่นเตรียมปั้ม(ซม.):</label 
              >
              <input
                type="text"
                id="name5"
                name="name5"
                class="border rounded px-4 py-2 w-3/4"
                v-model="formData.additional"
                placeholder="ใส่ค่าบวกเพิ่มเตรียมปั้ม" 
                required
              />
            </div>
            <div class="mb-4 flex flex-row items-center">
              <label for="has_filling" class="block text-gray-600 w-1/4"
                >ลังมีไส้หรือไม่:</label
              >
              <div class="w-3/4">
                <label for="has_filling_yes" class="inline-block mr-2"
                  >มี</label
                >
                <input
                  type="radio"
                  id="has_filling_yes"
                  name="has_filling"
                  value="1"
                  v-model="formData.hasIt"
                  required
                />
                <label for="has_filling_no" class="inline-block ml-4 mr-2"
                  >ไม่มี</label
                >
                <input
                  type="radio"
                  id="has_filling_no"
                  name="has_filling"
                  value="0"
                  v-model="formData.hasIt"
                  required 
                />
              </div>
            </div>
            <div v-if="formData.hasIt=== '1'">
            <div class="mb-4 flex flex-row items-center">
              <label for="name" class="block text-gray-600 w-1/4"
                >ใส่จำนวนช่องเเบ่งด้านกว้าง:</label
              >
              <input
                type="text"
                id="name6"
                name="name6"
                class="border rounded px-4 py-2 w-3/4"
                v-model="formData.amountofwidth"
                placeholder="ใส่จำนวนช่องเเบ่งด้านกว้าง"
                required
              />
            </div>
            <div class="mb-4 flex flex-row items-center">
              <label for="name" class="block text-gray-600 w-1/4"
                >ใส่จำนวนช่องเเบ่งด้านยาว:</label
              >
              <input
                type="text"
                id="name7"
                name="name7"
                class="border rounded px-4 py-2 w-3/4"
                v-model="formData.amountoflength"
                placeholder="ใส่จำนวนช่องเเบ่งด้านยาว"
                required 
              />
            </div>
            <div class="mb-4 flex flex-row items-center">
              <label for="name" class="block text-gray-600 w-1/4"
                >ใส่ค่าความหนาของเเผ่นกั้น(มม.):</label
                
              >
              <input
                type="text"
                id="name8"
                name="name8"
                class="border rounded px-4 py-2 w-3/4"
                v-model="formData.thickness"
                placeholder="ใส่ค่าความหนาของเเผ่นกั้น" 
                required
              />
            </div>
            <div class="mb-4 flex flex-row items-center">
              <label for="has_filling" class="block text-gray-600 w-1/4"
                >ชุดไส้ใช้ผนังลังร่วมหรือไม่:</label
              >
              <div class="w-3/4">
                <label for="has_filling_yes" class="inline-block mr-2"
                  >มี</label
                >
                <input
                  type="radio"
                  id="has_filling_yes1"
                  name="has_filling1"
                  value="yes"
                  v-model="formData.hasskin"
                  required
                />
                <label for="has_filling_no" class="inline-block ml-4 mr-2"
                  >ไม่มี</label
                >
                <input
                  type="radio"
                  id="has_filling_no1"
                  name="has_filling1"
                  value="no"
                  v-model="formData.hasskin"
                  required
                />
              </div>
            </div>
            </div>
          </div>
          <div class="layout-image">
            <img
              src="https://via.placeholder.com/250x250"
              alt="Image"
              class="w-50 h-50 mt-2 mb-2"
            />
            <br />
            <div class="mb-4 flex justify-center w-full">
              <input
                type="text"
                id="name9"
                name="name9"
                placeholder="ใส่ชื่อของกล่อง" 
                class="border rounded px-2 py-1 w-3/4"
              />
            </div>

            <div class="text-center mt-2">
              <button
                type="submit"
                class="bg-blue-500 text-white px-4 py-2 rounded mr-2 inline-block"
              >
                ยืนยัน
              </button>
              <button
                type="button"
                class="bg-red-500 text-white px-4 py-2 rounded inline-block"
               @click="resetForm"
              >
                ยกเลิก
              </button>
            </div>
          </div>
          <div></div>
        </div>
      </form>
    </div>

    <!-- Right Section -->
    <!-- <div class="w-1/2 p-8 flex flex-col items-center mt-4">
      <form @submit.prevent="submitForm" ref="rightForm"></form>
    </div> -->
  <!-- </div> -->
</template>

<script>







export default {
  name: "InputForm1",
  data(){
    return{
      typeList:[
        {id:'',label:'เลือกประเภท'},
        {id:'test1',label:'65x150'},
        {id:'test2',label:'65x245'},
        {id:'test3',label:'130x150'},
        {id:'test4',label:'150x180'},
        {id:'test5',label:'150x245'},
      ]
    };
  },
  computed: {
    formData: {
      get() {
        console.log( this.$store.getters.getFormData);
        return this.$store.getters.getFormData;
      },
      set(formData) {
        this.$store.dispatch("setFormData", formData);
      },
    },
  },
  methods: {
    async submitForm() {
       // ส่งค่าไป Vuex Store
      var _this = this; 
      this.$store.dispatch("setFormData", this.formData);
       console.log( this.$store.getters.getFormData);
      _this.$router.push('/t2'); 
      
     
    }, 
    resetForm() {
      // Reset form fields to their initial state
      this.formData = {
        width: "",
        length: "",
        height: "",
        thick: "",
        type: "",
        additional: "",
        hasIt: "",
        amountofwidth: "",
        amountoflength: "",
        thickness: "",
        hasskin: "" 
      };
    },
  },
}
</script>


<style scoped>
.custom-layout {
  display: grid;
  grid-template-columns: auto fit-content(100%) fit-content(100%) auto;
}
.layout-main{
  padding-right:60px ; 
}
</style>
