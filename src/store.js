// store.js
import { createStore } from 'vuex';

export default new createStore({
  state: {
    formData: {
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
      hasskin: "",
    },
    dOutput: {
      IW: 0.0,
      OW: 0.0,
      FL: 0.0,
      PL: 0.0,
      OO: 0.0, // Add OO with an initial value
      II: 0.0, // Add II with an initial value
      OP: 0.0, // Add OP with an initial value
      IP: 0.0, // Add IP with an initial value
      PW: 0.0, // Add PW with an initial value
      x: 0, // Add x with an initial value
      AW1: 0.0, // Add AW1 with an initial value
      AH1: 0.0, // Add AH1 with an initial value
    },
  },
  getters: {
    getFormData: (state) => state.formData,
    getFormOutput: (state) => state.dOutput,
  },
  mutations: {
    setFormData: (state, formData) => {
      state.formData = formData;
    },
    setOutput: (state, { IW, OW,FL,PL,OO,II,OP, IP, PW,x,AW1,AH1 }) => {
      state.dOutput.IW = IW;
      state.dOutput.OW = OW;
      state.dOutput.FL= FL;
      state.dOutput.PL = PL;
      state.dOutput.OO = OO; // Update OO
      state.dOutput.II = II; // Update II
      state.dOutput.OP = OP; // Update OP
      state.dOutput.IP = IP; // Update IP
      state.dOutput.PW = PW; // Update PW
      state.dOutput.x = x; // Update 
      state.dOutput.AW1 = AW1; // Update 
      state.dOutput.AH1 = AH1; // Update 
      

    },
  },
  actions: {
    setFormData: ({ commit }, formData) => {
      commit('setFormData', formData);
    },
    setOutput: ({ commit }, { IW, OW,FL,PL,OO,II,OP,IP,PW,AW1,AW2}) => {
      commit('setOutput', { IW, OW,FL,PL,OO,II,OP,IP,PW,AW1,AW2 });
    },
  },
});
