mapeamento_arquivos = {
    "Estabelecimentos": {
        "tabela": "TabEstabelecimentoArquivo",
        "colunas": [
            "teaCnpjBasico", "teaCnpjOrdem", "teaCnpjDV", "teaIdMatrizFilial", "teaNomeFantasia", "teaSituacaoCadastral",
            "teaDataSitCadastral", "teaMotivoSitCadastral", "teaNomeCidadeExterior", "teaPais", "teaDataInicioAtividade", "teaCnaePrincipal",
            "teaCnaeSecundario", "teaTipoLogradouro", "teaLogradouro", "teaNumero", "teaComplemento", "teaBairro", "teaCEP", "teaUF", "teaMunicipio",
            "teaDDD1", "teaTelefone1", "teaDDD2", "teaTelefone2", "teaDDDFax", "teaFax", "teaEmail", "teaSituacaoEspecial", "teaDataSitEspecial"
        ],
        "sep": ";",
        "encoding": "utf-8",
        "sequencia": 1,
        "filtroCNPJ": False
    },
    "Empresas": {
        "tabela": "TabEmpresaArquivo",
        "colunas": [
            "teoCnpjBasico", "teoRazaoSocial", "teoNatJuridica", 
            "teoQualificacaoResponsavel", "teoCapitalSocial", 
            "teoPorteEmpresa", "teoEnteFederativoRes"
        ],
        "sep": ";",
        "encoding": "utf-8",
        "sequencia": 2,
        "filtroCNPJ": True
    },
    "Cnaes": {
        "tabela": "TabCnaeArquivo",
        "colunas": [ "tcaCodigo", "tcaDescricao" ],
        "sep": ";",
        "encoding": "utf-8",
        "sequencia": 3,
        "filtroCNPJ": False        
    },
    "Motivos": {
        "tabela": "TabMotivoArquivo",
        "colunas": [ "tmoCodigo", "tmoDescricao" ],
        "sep": ";",
        "encoding": "utf-8",
        "sequencia": 4,
        "filtroCNPJ": False
    },
    "Qualificacoes": {
        "tabela": "TabQualificacaoSocioArquivo",
        "colunas": [
            "tqsCodigo", "tqsDescricao"
        ],
        "sep": ";",
        "encoding": "utf-8",
        "sequencia": 5,
        "filtroCNPJ": False
    },
    "Socios": {
        "tabela": "TabSocioArquivo",
        "colunas": [
            "tsaCnpjBasico", "tsaIdentificador", "tsaNomeSocio", "tsaCPFCNPJ", "tsaCodigoQualificacao", "tsaDataEntrada",
            "tsaPais", "tsaCPFRepresentanteLegal", "tsaNomeRepresentante", "tsaCodQualificacaoRepresentante", "tsaFaixaEtaria"
        ],
        "sep": ";",
        "encoding": "utf-8",
        "sequencia": 6,
        "filtroCNPJ": True
    },
    "Municipios": {
        "tabela": "TabMunicipioArquivo",
        "colunas": ["tmaCodigo", "tmaDescricao"],
        "sep": ";",
        "encoding": "utf-8",
        "sequencia": 7,
        "filtroCNPJ": False
    },
    "Paises": {
        "tabela": "TabPaisArquivo",
        "colunas": ["tpaCodigo", "tpaDescricao"],
        "sep": ";",
        "encoding": "utf-8",
        "sequencia": 8,
        "filtroCNPJ": False
    },
    "Simples": {
        "tabela": "TabSimplesArquivo",
        "colunas": ["tssCnpjBasico", "tssOpcaoSimples", "tssDataOpcaoSimples", "tssDataExclusaoSimples", "tssOpcaoMEI", "tssDataOpcaoMEI", "tssDataExclusaoMEI"],
        "sep": ";",
        "encoding": "utf-8",
        "sequencia": 9,
        "filtroCNPJ": True
    },
    "Naturezas": {
        "tabela": "TabNaturezaJuridicaArquivo",
        "colunas": ["tnjCodigo", "tnjDescricao"],
        "sep": ";",
        "encoding": "utf-8",
        "sequencia": 10,
        "filtroCNPJ": False
    }
}