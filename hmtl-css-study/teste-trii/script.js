const formulario = document.querySelector("form")
const nome = document.querySelector("#inputname")
const tel = document.querySelector("#inputtel")
const email = document.querySelector("#inputemail")
const textareamsg = document.querySelector("#msg")
const selectt = document.querySelector("#menu")
const camposubmit = document.querySelector(".sucess")

formulario.addEventListener("submit",function(evento){evento.preventDefault();
console.log("Botão clicado com sucesso e página travada!");
});
formulario.addEventListener("submit",enviar)
function enviar(e){
   if (nome.value.trim() === "") {
        nome.classList.add("campo-erro"); 
        nome.focus();
        
  
        nome.addEventListener('input', function() {
            if (nome.value.trim() !== "") {
                nome.classList.remove("campo-erro");
            }
        })};
if (tel.value.trim()===''){
        tel.classList.add
        ("campo-erro");
        tel.focus();
        tel.addEventListener('input', function() {
        if (tel.value.trim() !== "") {
            tel.classList.remove("campo-erro");}
        })};
    
if (email.value.trim()===''){
        email.classList.add
        ("campo-erro");
        email.focus();
        email.addEventListener('input', function() {
        if (email.value.trim() !== "") {
            email.classList.remove("campo-erro");}
        })};

if (textareamsg.value.trim()===''){
        textareamsg.classList.add
        ("campo-erro");
        textareamsg.focus();
        textareamsg.addEventListener('input', function() {
        if (textareamsg.value.trim() !== "") {
            textareamsg.classList.remove("campo-erro");}
        })};

if (selectt.value.trim()==='Escolha o serviço que deseja'){
        selectt.classList.add
        ("campo-erro");
        selectt.focus();
        selectt.addEventListener('change', function() {
        if (selectt.value.trim() !== "Escolha o serviço que deseja") {
            selectt.classList.remove("campo-erro");}
        });

        return;
}};


const meuFormulario = document.querySelector("form"); 
const msgSucesso = document.getElementById("mensagem-sucesso");

meuFormulario.addEventListener("submit", enviado);

function enviado(event) {
    event.preventDefault(); 

    if (
        nome.value.trim() !== "" && 
        tel.value.trim() !== "" && 
        email.value.trim() !== "" && 
        textareamsg.value.trim() !== "" && 
        selectt.value !== "Escolha o serviço que deseja"
    ) {
        // Adiciona a classe CSS que ativa a transição leve
        msgSucesso.classList.add("mostrar"); 
    }
}

