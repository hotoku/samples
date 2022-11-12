import "reflect-metadata";
import { Query, Resolver, Arg } from "type-graphql";
import { Team } from "./teams.schema";

export const teams = new Map<number, Team>();
for (let i = 0; i < 3; i++) {
  teams.set(i, { id: i, name: `team ${i}` });
}

@Resolver(() => Team)
export class TeamsResolver {
  @Query(() => Team)
  async getTeam(@Arg("id") id: number): Promise<Team | undefined> {
    const user = teams.get(id);
    return user;
  }
}
