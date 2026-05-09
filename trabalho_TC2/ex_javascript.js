const texto = "A reunião de alinhamento está marcada para 15/05/2026. O prazo final do projeto é 20/05/2026, não se atrase!";

const padraoDataGlobal = /\b\d{2}\/\d{2}\/\d{4}\b/g;
const padraoDataUnico = /\b\d{2}\/\d{2}\/\d{4}\b/;

const datasEncontradas = texto.match(padraoDataGlobal);
console.log("1. Datas encontradas na string:");
console.log(datasEncontradas);

const primeiraData = padraoDataUnico.exec(texto);
if (primeiraData) {
    console.log("\n2. Primeira data encontrada:");
    console.log(`Valor: ${primeiraData[0]} (Inicia no índice ${primeiraData.index})`);
}

const textoCensurado = texto.replace(padraoDataGlobal, '[DATA OCULTA]');
console.log("\n3. Texto com as datas substituídas:");
console.log(textoCensurado);
