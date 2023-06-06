# GraphQL + TypeScript + expressの例

GraphQLの学習用。

## 動かし方

1. npm i
1. npm run create-db
1. npm run start
1. http://localhost:4000/graphiql にアクセス
1. 以下のようなクエリ例を発行してみる

**例**

``` graphql
query {
  getUser(id: 1) {
    name
    team {
      name
      users {
        name
        team {
          name
          users {
            name
            team {
              name
            }
          }
        }
      }
    }
  }
  getTeam(id: 1) {
    name
    users {
      name
    }
  }
}
```
