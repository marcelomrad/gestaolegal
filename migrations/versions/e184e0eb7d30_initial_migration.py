"""Initial migration

Revision ID: e184e0eb7d30
Revises: 
Create Date: 2021-10-05 12:38:03.757721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e184e0eb7d30'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('arquivos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titulo', sa.String(length=150, collation='latin1_general_ci'), nullable=False),
    sa.Column('descricao', sa.String(length=8000, collation='latin1_general_ci'), nullable=True),
    sa.Column('nome', sa.Text(collation='latin1_general_ci'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dias_plantao',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.Date(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('documentos_roteiro',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('area_direito', sa.String(length=50, collation='latin1_general_ci'), nullable=False),
    sa.Column('link', sa.String(length=1000, collation='latin1_general_ci'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('enderecos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('logradouro', sa.String(length=100, collation='latin1_general_ci'), nullable=False),
    sa.Column('numero', sa.String(length=8, collation='latin1_general_ci'), nullable=False),
    sa.Column('complemento', sa.String(length=100, collation='latin1_general_ci'), nullable=True),
    sa.Column('bairro', sa.String(length=100, collation='latin1_general_ci'), nullable=False),
    sa.Column('cep', sa.String(length=9, collation='latin1_general_ci'), nullable=False),
    sa.Column('cidade', sa.String(length=100, collation='latin1_general_ci'), nullable=False),
    sa.Column('estado', sa.String(length=100, collation='latin1_general_ci'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orientacao_juridica',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('area_direito', sa.String(length=50, collation='latin1_general_ci'), nullable=False),
    sa.Column('sub_area', sa.String(length=50, collation='latin1_general_ci'), nullable=True),
    sa.Column('descricao', sa.String(length=1001, collation='latin1_general_ci'), nullable=False),
    sa.Column('data_criacao', sa.DateTime(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('plantao',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_abertura', sa.DateTime(), nullable=True),
    sa.Column('data_fechamento', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('assistencias_judiciarias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=150, collation='latin1_general_ci'), nullable=False),
    sa.Column('regiao', sa.String(length=80, collation='latin1_general_ci'), nullable=False),
    sa.Column('areas_atendidas', sa.String(length=1000, collation='latin1_general_ci'), nullable=False),
    sa.Column('endereco_id', sa.Integer(), nullable=True),
    sa.Column('telefone', sa.String(length=18, collation='latin1_general_ci'), nullable=False),
    sa.Column('email', sa.String(length=80, collation='latin1_general_ci'), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['endereco_id'], ['enderecos.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('atendidos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=80, collation='latin1_general_ci'), nullable=False),
    sa.Column('data_nascimento', sa.Date(), nullable=False),
    sa.Column('cpf', sa.String(length=14, collation='latin1_general_ci'), nullable=False),
    sa.Column('cnpj', sa.String(length=18, collation='latin1_general_ci'), nullable=True),
    sa.Column('endereco_id', sa.Integer(), nullable=True),
    sa.Column('telefone', sa.String(length=18, collation='latin1_general_ci'), nullable=True),
    sa.Column('celular', sa.String(length=18, collation='latin1_general_ci'), nullable=False),
    sa.Column('email', sa.String(length=80, collation='latin1_general_ci'), nullable=False),
    sa.Column('estado_civil', sa.String(length=80, collation='latin1_general_ci'), nullable=False),
    sa.Column('como_conheceu', sa.String(length=80, collation='latin1_general_ci'), nullable=False),
    sa.Column('indicacao_orgao', sa.String(length=80, collation='latin1_general_ci'), nullable=True),
    sa.Column('procurou_outro_local', sa.String(length=80, collation='latin1_general_ci'), nullable=False),
    sa.Column('procurou_qual_local', sa.String(length=80, collation='latin1_general_ci'), nullable=True),
    sa.Column('obs', sa.Text(collation='latin1_general_ci'), nullable=True),
    sa.Column('pj_constituida', sa.String(length=80, collation='latin1_general_ci'), nullable=False),
    sa.Column('repres_legal', sa.Boolean(), nullable=True),
    sa.Column('nome_repres_legal', sa.String(length=80, collation='latin1_general_ci'), nullable=True),
    sa.Column('cpf_repres_legal', sa.String(length=14, collation='latin1_general_ci'), nullable=True),
    sa.Column('contato_repres_legal', sa.String(length=18, collation='latin1_general_ci'), nullable=True),
    sa.Column('rg_repres_legal', sa.String(length=50, collation='latin1_general_ci'), nullable=True),
    sa.Column('nascimento_repres_legal', sa.Date(), nullable=True),
    sa.Column('pretende_constituir_pj', sa.String(length=80, collation='latin1_general_ci'), nullable=True),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['endereco_id'], ['enderecos.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=80, collation='latin1_general_ci'), nullable=False),
    sa.Column('senha', sa.String(length=60, collation='latin1_general_ci'), nullable=False),
    sa.Column('urole', sa.String(length=50, collation='latin1_general_ci'), nullable=False),
    sa.Column('nome', sa.String(length=60, collation='latin1_general_ci'), nullable=False),
    sa.Column('sexo', sa.String(length=60, collation='latin1_general_ci'), nullable=False),
    sa.Column('rg', sa.String(length=18, collation='latin1_general_ci'), nullable=False),
    sa.Column('cpf', sa.String(length=14, collation='latin1_general_ci'), nullable=False),
    sa.Column('profissao', sa.String(length=45, collation='latin1_general_ci'), nullable=False),
    sa.Column('estado_civil', sa.String(length=45, collation='latin1_general_ci'), nullable=False),
    sa.Column('nascimento', sa.Date(), nullable=False),
    sa.Column('telefone', sa.String(length=18, collation='latin1_general_ci'), nullable=True),
    sa.Column('celular', sa.String(length=18, collation='latin1_general_ci'), nullable=False),
    sa.Column('oab', sa.String(length=30, collation='latin1_general_ci'), nullable=True),
    sa.Column('obs', sa.Text(collation='latin1_general_ci'), nullable=True),
    sa.Column('data_entrada', sa.Date(), nullable=False),
    sa.Column('data_saida', sa.Date(), nullable=True),
    sa.Column('criado', sa.DateTime(), nullable=False),
    sa.Column('modificado', sa.DateTime(), nullable=True),
    sa.Column('criadopor', sa.Integer(), nullable=False),
    sa.Column('matricula', sa.String(length=45, collation='latin1_general_ci'), nullable=True),
    sa.Column('modificadopor', sa.Integer(), nullable=True),
    sa.Column('bolsista', sa.Boolean(), nullable=False),
    sa.Column('tipo_bolsa', sa.String(length=50, collation='latin1_general_ci'), nullable=True),
    sa.Column('horario_atendimento', sa.String(length=30, collation='latin1_general_ci'), nullable=True),
    sa.Column('suplente', sa.String(length=30, collation='latin1_general_ci'), nullable=True),
    sa.Column('ferias', sa.String(length=150, collation='latin1_general_ci'), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('cert_atuacao_DAJ', sa.String(length=3, collation='latin1_general_ci'), nullable=False),
    sa.Column('inicio_bolsa', sa.DateTime(), nullable=True),
    sa.Column('fim_bolsa', sa.DateTime(), nullable=True),
    sa.Column('endereco_id', sa.Integer(), nullable=True),
    sa.Column('chave_recuperacao', sa.Boolean(), server_default=sa.text('false'), nullable=True),
    sa.ForeignKeyConstraint(['endereco_id'], ['enderecos.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('assistenciasJudiciarias_xOrientacao_juridica',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_orientacaoJuridica', sa.Integer(), nullable=True),
    sa.Column('id_assistenciaJudiciaria', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_assistenciaJudiciaria'], ['assistencias_judiciarias.id'], ),
    sa.ForeignKeyConstraint(['id_orientacaoJuridica'], ['orientacao_juridica.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('assistidos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_atendido', sa.Integer(), nullable=True),
    sa.Column('sexo', sa.String(length=1, collation='latin1_general_ci'), nullable=False),
    sa.Column('profissao', sa.String(length=80, collation='latin1_general_ci'), nullable=False),
    sa.Column('raca', sa.String(length=20, collation='latin1_general_ci'), nullable=False),
    sa.Column('rg', sa.String(length=50, collation='latin1_general_ci'), nullable=False),
    sa.Column('grau_instrucao', sa.String(length=100, collation='latin1_general_ci'), nullable=False),
    sa.Column('salario', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('beneficio', sa.String(length=30, collation='latin1_general_ci'), nullable=False),
    sa.Column('qual_beneficio', sa.String(length=30, collation='latin1_general_ci'), nullable=True),
    sa.Column('contribui_inss', sa.String(length=20, collation='latin1_general_ci'), nullable=False),
    sa.Column('qtd_pessoas_moradia', sa.Integer(), nullable=False),
    sa.Column('renda_familiar', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('participacao_renda', sa.String(length=100, collation='latin1_general_ci'), nullable=False),
    sa.Column('tipo_moradia', sa.String(length=100, collation='latin1_general_ci'), nullable=False),
    sa.Column('possui_outros_imoveis', sa.Boolean(), nullable=False),
    sa.Column('quantos_imoveis', sa.Integer(), nullable=True),
    sa.Column('possui_veiculos', sa.Boolean(), nullable=False),
    sa.Column('possui_veiculos_obs', sa.String(length=100, collation='latin1_general_ci'), nullable=True),
    sa.Column('quantos_veiculos', sa.Integer(), nullable=True),
    sa.Column('ano_veiculo', sa.String(length=5, collation='latin1_general_ci'), nullable=True),
    sa.Column('doenca_grave_familia', sa.String(length=20, collation='latin1_general_ci'), nullable=False),
    sa.Column('pessoa_doente', sa.String(length=50, collation='latin1_general_ci'), nullable=True),
    sa.Column('pessoa_doente_obs', sa.String(length=100, collation='latin1_general_ci'), nullable=True),
    sa.Column('gastos_medicacao', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('obs', sa.String(length=1000, collation='latin1_general_ci'), nullable=True),
    sa.ForeignKeyConstraint(['id_atendido'], ['atendidos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('atendido_xOrientacaoJuridica',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_orientacaoJuridica', sa.Integer(), nullable=True),
    sa.Column('id_atendido', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_atendido'], ['atendidos.id'], ),
    sa.ForeignKeyConstraint(['id_orientacaoJuridica'], ['orientacao_juridica.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('casos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_usuario_responsavel', sa.Integer(), nullable=False),
    sa.Column('area_direito', sa.String(length=50, collation='latin1_general_ci'), nullable=False),
    sa.Column('sub_area', sa.String(length=50, collation='latin1_general_ci'), nullable=True),
    sa.Column('id_orientador', sa.Integer(), nullable=True),
    sa.Column('id_estagiario', sa.Integer(), nullable=True),
    sa.Column('id_colaborador', sa.Integer(), nullable=True),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('id_criado_por', sa.Integer(), nullable=False),
    sa.Column('data_modificacao', sa.DateTime(), nullable=True),
    sa.Column('id_modificado_por', sa.Integer(), nullable=True),
    sa.Column('situacao_deferimento', sa.String(length=50, collation='latin1_general_ci'), nullable=False),
    sa.Column('justif_indeferimento', sa.String(length=280, collation='latin1_general_ci'), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('descricao', sa.Text(collation='latin1_general_ci'), nullable=True),
    sa.Column('numero_ultimo_processo', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_colaborador'], ['usuarios.id'], ),
    sa.ForeignKeyConstraint(['id_criado_por'], ['usuarios.id'], ),
    sa.ForeignKeyConstraint(['id_estagiario'], ['usuarios.id'], ),
    sa.ForeignKeyConstraint(['id_modificado_por'], ['usuarios.id'], ),
    sa.ForeignKeyConstraint(['id_orientador'], ['usuarios.id'], ),
    sa.ForeignKeyConstraint(['id_usuario_responsavel'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dias_marcados_plantao',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_marcada', sa.Date(), nullable=True),
    sa.Column('confirmacao', sa.String(length=15, collation='latin1_general_ci'), nullable=False),
    sa.Column('id_usuario', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_usuario'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('notificacao',
    sa.Column('id_executor_acao', sa.Integer(), nullable=True),
    sa.Column('id_usu_notificar', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('acao', sa.String(length=200, collation='latin1_general_ci'), nullable=False),
    sa.Column('data', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['id_executor_acao'], ['usuarios.id'], ),
    sa.ForeignKeyConstraint(['id_usu_notificar'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('registro_entrada',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data_entrada', sa.DateTime(), nullable=False),
    sa.Column('data_saida', sa.DateTime(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('confirmacao', sa.String(length=15, collation='latin1_general_ci'), nullable=False),
    sa.Column('id_usuario', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_usuario'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('arquivosCaso',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('link_arquivo', sa.String(length=300, collation='latin1_general_ci'), nullable=True),
    sa.Column('id_caso', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_caso'], ['casos.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('assistidos_pessoa_juridica',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_assistido', sa.Integer(), nullable=True),
    sa.Column('socios', sa.String(length=1000, collation='latin1_general_ci'), nullable=True),
    sa.Column('situacao_receita', sa.String(length=100, collation='latin1_general_ci'), nullable=False),
    sa.Column('enquadramento', sa.String(length=100, collation='latin1_general_ci'), nullable=False),
    sa.Column('sede_bh', sa.Boolean(), nullable=False),
    sa.Column('regiao_sede_bh', sa.String(length=50, collation='latin1_general_ci'), nullable=True),
    sa.Column('regiao_sede_outros', sa.String(length=100, collation='latin1_general_ci'), nullable=True),
    sa.Column('area_atuacao', sa.String(length=50, collation='latin1_general_ci'), nullable=False),
    sa.Column('negocio_nascente', sa.Boolean(), nullable=False),
    sa.Column('orgao_registro', sa.String(length=100, collation='latin1_general_ci'), nullable=False),
    sa.Column('faturamento_anual', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('ultimo_balanco_neg', sa.String(length=50, collation='latin1_general_ci'), nullable=True),
    sa.Column('resultado_econ_neg', sa.String(length=50, collation='latin1_general_ci'), nullable=True),
    sa.Column('tem_funcionarios', sa.String(length=20, collation='latin1_general_ci'), nullable=False),
    sa.Column('qtd_funcionarios', sa.String(length=7, collation='latin1_general_ci'), nullable=True),
    sa.ForeignKeyConstraint(['id_assistido'], ['assistidos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('casos_atendidos',
    sa.Column('id_caso', sa.Integer(), nullable=True),
    sa.Column('id_atendido', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_atendido'], ['atendidos.id'], ),
    sa.ForeignKeyConstraint(['id_caso'], ['casos.id'], )
    )
    op.create_table('eventos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_caso', sa.Integer(), nullable=False),
    sa.Column('num_evento', sa.Integer(), nullable=True),
    sa.Column('tipo', sa.String(length=50, collation='latin1_general_ci'), nullable=False),
    sa.Column('descricao', sa.String(length=1001, collation='latin1_general_ci'), nullable=True),
    sa.Column('arquivo', sa.String(length=100, collation='latin1_general_ci'), nullable=True),
    sa.Column('data_evento', sa.Date(), nullable=False),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('id_criado_por', sa.Integer(), nullable=False),
    sa.Column('id_usuario_responsavel', sa.Integer(), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['id_caso'], ['casos.id'], ),
    sa.ForeignKeyConstraint(['id_criado_por'], ['usuarios.id'], ),
    sa.ForeignKeyConstraint(['id_usuario_responsavel'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('historicos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_usuario', sa.Integer(), nullable=False),
    sa.Column('id_caso', sa.Integer(), nullable=False),
    sa.Column('data', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['id_caso'], ['casos.id'], ),
    sa.ForeignKeyConstraint(['id_usuario'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('lembretes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_do_criador', sa.Integer(), nullable=False),
    sa.Column('id_caso', sa.Integer(), nullable=False),
    sa.Column('id_usuario', sa.Integer(), nullable=False),
    sa.Column('data_criacao', sa.DateTime(), nullable=False),
    sa.Column('data_lembrete', sa.DateTime(), nullable=False),
    sa.Column('descricao', sa.String(length=1001, collation='latin1_general_ci'), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['id_caso'], ['casos.id'], ),
    sa.ForeignKeyConstraint(['id_do_criador'], ['usuarios.id'], ),
    sa.ForeignKeyConstraint(['id_usuario'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('processos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('especie', sa.String(length=25, collation='latin1_general_ci'), nullable=False),
    sa.Column('numero', sa.Integer(), nullable=True),
    sa.Column('identificacao', sa.Text(collation='latin1_general_ci'), nullable=True),
    sa.Column('vara', sa.String(length=200, collation='latin1_general_ci'), nullable=True),
    sa.Column('link', sa.String(length=1000, collation='latin1_general_ci'), nullable=True),
    sa.Column('probabilidade', sa.String(length=25, collation='latin1_general_ci'), nullable=True),
    sa.Column('posicao_assistido', sa.String(length=25, collation='latin1_general_ci'), nullable=True),
    sa.Column('valor_causa_inicial', sa.Integer(), nullable=True),
    sa.Column('valor_causa_atual', sa.Integer(), nullable=True),
    sa.Column('data_distribuicao', sa.Date(), nullable=True),
    sa.Column('data_transito_em_julgado', sa.Date(), nullable=True),
    sa.Column('obs', sa.Text(collation='latin1_general_ci'), nullable=True),
    sa.Column('id_caso', sa.Integer(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('id_criado_por', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_caso'], ['casos.id'], ),
    sa.ForeignKeyConstraint(['id_criado_por'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('numero')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('processos')
    op.drop_table('lembretes')
    op.drop_table('historicos')
    op.drop_table('eventos')
    op.drop_table('casos_atendidos')
    op.drop_table('assistidos_pessoa_juridica')
    op.drop_table('arquivosCaso')
    op.drop_table('registro_entrada')
    op.drop_table('notificacao')
    op.drop_table('dias_marcados_plantao')
    op.drop_table('casos')
    op.drop_table('atendido_xOrientacaoJuridica')
    op.drop_table('assistidos')
    op.drop_table('assistenciasJudiciarias_xOrientacao_juridica')
    op.drop_table('usuarios')
    op.drop_table('atendidos')
    op.drop_table('assistencias_judiciarias')
    op.drop_table('plantao')
    op.drop_table('orientacao_juridica')
    op.drop_table('enderecos')
    op.drop_table('documentos_roteiro')
    op.drop_table('dias_plantao')
    op.drop_table('arquivos')
    # ### end Alembic commands ###
