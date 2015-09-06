# CU-KG
Content Understanding - Knowledge Graph

## Web Application
- Frontend: Just Bootstrap(Flask-Bootstrap)
- Backend: Flask

### Flask Blueprint
- auth 身份认证(Flask-Auth)
  - login
  - register
  - permission
  - user zone
    - CRUD log(admin)
- entity_base 知识库
  - related entity
  - related relation
  - attribute
    - common
    - picture
    - video
  - graph(sigmajs)
- control_board 控制台
  - classified triplet CRUD(DataTables)
    - is-a and instance-of
    - "attribute" prefixed
    - common predicate
  - import triplets by file(Excel...)
- relation_search 关系搜索
- about 关于
  - introduction
  - entity count and relation count
  - classification

## Database
- Frontend Database: Cayley(Graph Database)
- Backend Database: MongoDB(Document Database)

