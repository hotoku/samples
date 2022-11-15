type TeamResolver = {
  id: number;
  name: string;
  users: () => Promise<UserResolver[]>;
};

type UserResolver = {
  id: number;
  name: string;
  team: () => Promise<TeamResolver>;
};

export async function getUser(
  _: any,
  args: { id: number },
  context: any
): Promise<UserResolver> {
  const user = await context.userLoader.load(args.id);
  return {
    id: args.id,
    name: user.name,
    team: async () => getTeam({ id: user.teamId }),
  };
}

export async function getTeam(
  _: any,
  args: { id: number },
  context: any
): Promise<TeamResolver> {
  const team = await context.teamLoader.load(args.id);
  return {
    id: args.id,
    name: team.name,
    users: async () => Promise.all(team.userIds.map((id) => getUser({ id }))),
  };
}
