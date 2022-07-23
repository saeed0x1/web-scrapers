import axios from "axios";
import jsdom from "jsdom";
import {parse} from "node-html-parser";
const { JSDOM } = jsdom;

(async ()=>{
    const res = await axios.get("http://127.0.0.1:5500/index.html");
    const resData = await res.data;
    
    // console.log(resData)
    const dom = new JSDOM(resData);
    
    const td = [];
    const allElements = [];
    const allsep = [];
    const companyNames = [];
    const contact = [];
    const country = [];

    const querySelect =(query)=>dom.window.document.querySelectorAll(query);

    const tableTr = querySelect("td");
    // const findTd = tableTr.children("td")
    tableTr.forEach((element)=>console.log(element.textContent))
    
    // tableTr.forEach((element)=>allElements.push(element.innerHTML.trim()))
  
    // console.log(allElements)
})();