import "reflect-metadata";
import { Query, Resolver, Mutation, Arg } from "type-graphql";
import { TeamInput, Team } from "./teams.schema";

@Resolver(() => Team)
export class TeamsResolver {
  private users: Team[] = [
    { id: 1, name: "team 1" },
    { id: 2, name: "team 2" },
    { id: 3, name: "team 3" },
  ];
  @Query(() => [Team])
  async getTeams(): Promise<Team[]> {
    return this.users;
  }
  @Query(() => Team)
  async getTeam(@Arg("id") id: number): Promise<Team | undefined> {
    const user = this.users.find((u) => u.id == id);
    return user;
  }
  @Mutation(() => Team)
  async updateTeam(
    @Arg("id") id: number,
    @Arg("input") input: TeamInput
  ): Promise<Team> {
    const user = this.users.find((u) => u.id == id);
    if (!user) {
      throw new Error("Team not found");
    }
    const updatedTeam = {
      ...user,
      ...input,
    };
    this.users = this.users.map((u) => (u.id === id ? updatedTeam : u));
    return updatedTeam;
  }
}
