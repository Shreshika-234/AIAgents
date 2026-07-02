from agents.supervisor import SupervisorAgent


def main():

    supervisor = SupervisorAgent(
        excel_path="data/leads.xlsx"
    )
    supervisor.run()


if __name__ == "__main__":

    main()