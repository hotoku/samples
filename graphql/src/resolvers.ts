import {
  GraphQLID,
  GraphQLInt,
  GraphQLList,
  GraphQLNonNull,
  GraphQLObjectType,
  GraphQLString,
} from "graphql";

import { UserRecord, TeamRecord, MyDataLoader } from "./data-loaders";

export const UserType: GraphQLObjectType<
  UserRecord,
  { loaders: MyDataLoader }
> = new GraphQLObjectType<UserRecord, { loaders: MyDataLoader }>({
  name: "User",
  fields: () => ({
    id: {
      type: GraphQLID,
    },
    name: {
      type: GraphQLString,
    },
    teamId: {
      type: GraphQLInt,
    },
    team: {
      type: TeamType,
      resolve: (obj, _, { loaders }, __) => {
        return loaders.teamLoader.load(obj.teamId);
      },
    },
  }),
});

export const TeamType: GraphQLObjectType<
  TeamRecord,
  { loaders: MyDataLoader }
> = new GraphQLObjectType<TeamRecord, { loaders: MyDataLoader }>({
  name: "Team",
  fields: () => ({
    id: {
      type: GraphQLID,
    },
    name: {
      type: GraphQLString,
    },
    users: {
      type: new GraphQLList(UserType),
      resolve: async (obj, _, { loaders }, __) => {
        const userIds = await loaders.teamUsersLoader.load(obj.id);
        const ps = [];
        for (const id of userIds) {
          ps.push(loaders.userLoader.load(id));
        }
        const ret = await Promise.all(ps);
        return ret;
      },
    },
  }),
});

export const queryType = new GraphQLObjectType<{}, { loaders: MyDataLoader }>({
  name: "Query",
  fields: {
    getUser: {
      type: UserType,
      args: {
        id: {
          type: new GraphQLNonNull(GraphQLInt),
        },
      },
      resolve: (_, args, { loaders }) => loaders.userLoader.load(args.id),
    },
    getTeam: {
      type: TeamType,
      args: {
        id: {
          type: new GraphQLNonNull(GraphQLInt),
        },
      },
      resolve: (_, args, { loaders }) => loaders.teamLoader.load(args.id),
    },
  },
});
