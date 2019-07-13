const baseURL = 'https://exceed.superposition.pknn.dev'
let state = {'HeartRate' : 0, 'Temp' : 0}
function get_data(){
    fetch (baseURL + '/data/group_one')
      .then((res) => res.text())
      .then((data) => state = JSON.parse(data))
      .catch((err) => console.log(err));
}

results = ""; // array for storing results
/*file inputs*/
inputs = document.getElementById('file1');
get_data();

//here I would like to write down all results
var btn = document.getElementById('saveBtn');

function readFile() {
    if (inputs.files && inputs.files[0]) {
        var FR = new FileReader();
        FR.onload = function (event) {
            results = event.target.result;
            showResult();
        };
        FR.readAsText(inputs.files[0]);
    }
}

btn.onclick = function () {
    readFile();
}

function showResult() {
    console.log(state['HeartRate'])
    console.log(state['Temp'])
    //Reset
    //Clear Result Sector
    let elem = document.getElementsByClassName("rate1")[0];
    elem.style.background = "#FFFFFF";
    elem = document.getElementsByClassName("rate2")[0];
    elem.style.background = "#FFFFFF";
    elem = document.getElementsByClassName("rate3")[0];
    elem.style.background = "#FFFFFF";
    elem = document.getElementsByClassName("rate4")[0];
    elem.style.background = "#FFFFFF";
    //Clear Patient Data
    let patient_block = document.getElementById("p-data");
    patient_block.parentNode.removeChild(patient_block);
    //Create New Patient Data
    patient_block = document.createElement("div");
    patient_block.setAttribute("id", "p-data");
    document.getElementsByClassName("block_p")[0].appendChild(patient_block);
    //Clear Question Sector
    let question_block = document.getElementById("q-list");
    question_block.parentNode.removeChild(question_block);
    //Create New Question Sector
    question_block = document.createElement("div");
    question_block.setAttribute("id", "q-list");
    document.getElementsByClassName("block_q")[0].appendChild(question_block);
    //["Question","Choice1","Choice2","Choice3","Choice4","Answer"]
    //['#']
    //['Score']
    //['Data']
    //Split Question
    let tmpM = results.split("\n");
    //Variable Init
    let tmp = [];
    let div_con;
    let div_row;
    let div_col;
    let div_ch;
    let index;
    //Question Sector
    for (var i = 0; i < tmpM.length; i++) {
        if (tmpM[i].length == 2) {
            index = i + 1;
            break;
        }
        //Set List
        tmp = tmpM[i].split("/")
        console.log(tmp)
        //Question
        div_con = document.createElement("div");
        div_con.classList.add("container");
        div_con.appendChild(document.createTextNode("(" + (i + 1) + ") " + tmp[0]));
        div_row = document.createElement("div");
        div_row.classList.add("row");
        //Choice 1
        div_ch = document.createElement("div");
        div_ch.appendChild(document.createTextNode(" • " + tmp[1]));
        if (tmp[5] == 1) {
            div_ch.classList.add("answer");
        } else {div_ch.classList.add("question");}
        div_col = document.createElement("div");
        div_col.classList.add("col-12");
        div_col.appendChild(div_ch);
        div_row.appendChild(div_col);
        div_row.style.animationName = "addfadechoice";
        div_row.style.animationDuration = "2s";
        //Choice 2
        div_ch = document.createElement("div");
        div_ch.appendChild(document.createTextNode(" • " + tmp[2]));
        if (tmp[5] == 2) {
            div_ch.classList.add("answer");
        } else {div_ch.classList.add("question");}
        div_col = document.createElement("div");
        div_col.classList.add("col-12");
        div_col.appendChild(div_ch);
        div_row.appendChild(div_col);
        div_row.style.animationName = "addfadechoice";
        div_row.style.animationDuration = "2s";
        //Choice 3
        div_ch = document.createElement("div");
        div_ch.appendChild(document.createTextNode(" • " + tmp[3]));
        if (tmp[5] == 3) {
            div_ch.classList.add("answer");
        } else {div_ch.classList.add("question");}
        div_col = document.createElement("div");
        div_col.classList.add("col-12");
        div_col.appendChild(div_ch);
        div_row.appendChild(div_col);
        div_row.style.animationName = "addfadechoice";
        div_row.style.animationDuration = "2s";
        //Choice 4
        div_ch = document.createElement("div");
        div_ch.appendChild(document.createTextNode(" • " + tmp[4]));
        if (tmp[5] == 4) {
            div_ch.classList.add("answer");
        } else {div_ch.classList.add("question");}
        div_col = document.createElement("div");
        div_col.classList.add("col-12");
        div_col.appendChild(div_ch);
        div_row.appendChild(div_col);
        div_row.style.animationName = "addfadechoice";
        div_row.style.animationDuration = "2s";
        //Merge
        div_con.appendChild(div_row);
        div_con.style.animationName = "addfadequest";
        div_con.style.animationDuration = "1s";
        //Done
        question_block.appendChild(div_con);
        question_block.appendChild(document.createElement("hr"));
        question_block.style.animationName = "addfadequest";
        question_block.style.animationDuration = "1s";
    }
    //Result Sector
    const score = tmpM[index];
    if (score < 7) { 
        elem = document.getElementsByClassName("rate1")[0]
        elem.style.animationName = "addfaderesult1";
        elem.style.animationDuration = "4s";
        elem.style.background = "#00FF33";
    }
    else if (score <= 12 ) {
        elem = document.getElementsByClassName("rate2")[0]
        elem.style.animationName = "addfaderesult2";
        elem.style.animationDuration = "4s";
        elem.style.background = "#66CC99";
    }
    else if (score <= 18 ) {
        elem = document.getElementsByClassName("rate3")[0]
        elem.style.animationName = "addfaderesult3";
        elem.style.animationDuration = "4s";
        elem.style.background = "#3366CC";
    }
    else {
        elem = document.getElementsByClassName("rate4")[0]
        elem.style.animationName = "addfaderesult4";
        elem.style.animationDuration = "4s";
        elem.style.background = "#333366";
    }
    //Patient Data
    for (var i = index + 1; i < tmpM.length; i++) {
        console.log(tmpM[i]);
        patient_block.appendChild(document.createTextNode(tmpM[i]));
        patient_block.appendChild(document.createElement("br"));
        patient_block.style.animationName = "addfadechoice";
        patient_block.style.animationDuration = "4s";
    }
}
