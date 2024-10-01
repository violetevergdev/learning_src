from src.db.db_connection import engine, Session, Base
from src.models.models import Workers, Resumes, Workload
from sqlalchemy import select, func, cast, Integer, and_, insert
from sqlalchemy.orm import aliased, joinedload, selectinload, contains_eager

def create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def insert_workers():
    worker_bob = Workers(username='Bob')
    worker_max = Workers(username='Max')
    with Session() as session:
        session.add_all([worker_bob, worker_max])
        session.commit()

def select_workers():
    with Session() as session:
        query = select(Workers)
        res = session.execute(query)
        workers = res.scalars().all()
        print(f"{workers=}")


def update_workers(worker_id: int = 2, new_username: str = 'Yarik'):
 with Session() as session:
    worker = session.get(Workers, worker_id)
    worker.username = new_username
    session.commit()
    print(f"{worker=}")

def insert_resumes():
    with Session() as session:
        resume_bob_1 = Resumes(
            title="Python Junior Developer", compensation=50000, workload=Workload.fulltime, worker_id=1)
        resume_bob_2 = Resumes(
            title="Python Разработчик", compensation=150000, workload=Workload.fulltime, worker_id=1)
        resume_max_1 = Resumes(
            title="Python Data Engineer", compensation=250000, workload=Workload.parttime, worker_id=2)
        resume_max_2 = Resumes(
            title="Data Scientist", compensation=300000, workload=Workload.fulltime, worker_id=2)
        session.add_all([resume_bob_1, resume_bob_2,
                         resume_max_1, resume_max_2])
        session.commit()

def select_resumes_avg_compensation(some_lang: str = 'Python'):
    with Session() as session:
        query = (
            select(
                Resumes.workload,
                cast(func.avg(Resumes.compensation), Integer).label('avg_compensation'),
            )
            .select_from(Resumes)
            .filter(and_(
                Resumes.title.contains(some_lang),
                Resumes.compensation > 40000
            ))
            .group_by(Resumes.workload)
        )
        print(query.compile(compile_kwargs={"literal_binds": True}))
        res = session.execute(query).all()
        print(f"{res=}")

def insert_additional_resumes():
        with Session() as session:
            workers = [
                {"username": "Artem"},  # id 3
                {"username": "Roman"},  # id 4
                {"username": "Petr"},  # id 5
            ]
            resumes = [
                {"title": "Python программист", "compensation": 60000, "workload": "fulltime", "worker_id": 3},
                {"title": "Machine Learning Engineer", "compensation": 70000, "workload": "parttime", "worker_id": 3},
                {"title": "Python Data Scientist", "compensation": 80000, "workload": "parttime", "worker_id": 4},
                {"title": "Python Analyst", "compensation": 90000, "workload": "fulltime", "worker_id": 4},
                {"title": "Python Junior Developer", "compensation": 100000, "workload": "fulltime", "worker_id": 5},
            ]
            insert_workers = insert(Workers).values(workers)
            insert_resumes = insert(Resumes).values(resumes)
            session.execute(insert_workers)
            session.execute(insert_resumes)
            session.commit()
def join_cte_subquery_func():
    with Session() as session:
        r = aliased(Resumes)
        w = aliased(Workers)

        subq = (
            select(
                r,
                w,
                cast(func.avg(r.compensation).over(partition_by=r.workload), Integer).label('avg_wl_compensation'),
                   )
            .join(r, r.worker_id == w.id).subquery('helper1')
        )
        cte = (
            select(
                subq.c.id,
                subq.c.username,
                subq.c.compensation,
                subq.c.workload,
                subq.c.avg_wl_compensation,
                (subq.c.compensation - subq.c.avg_wl_compensation).label('compensation_diff'),

            )
            .cte('helper2')
        )

        query = (
            select(cte)
            .order_by(cte.c.compensation_diff.desc())
        )

        print(query.compile(compile_kwargs={"literal_binds": True}))

        res = session.execute(query).all()
        print(f"{res=}")


def select_workers_with_lazy_relationship():
    with Session() as session:
        query = (
            select(Workers)
        )

        res = session.execute(query).scalars().all()

        worker_1_resumes = res[0].resumes
        print(f"{worker_1_resumes=}")

        worker_2_resumes = res[0].resumes
        print(f"{worker_2_resumes=}")


def select_workers_with_joined_relationship():
    with Session() as session:
        query = (
            select(Workers)
            .options(joinedload(Workers.resumes))
        )
        
        
        res = session.execute(query).unique().scalars().all()

        worker_1_resumes = res[0].resumes
        print(f"{worker_1_resumes=}")

        worker_2_resumes = res[0].resumes
        print(f"{worker_2_resumes=}")


def select_workers_with_selecting_relationship():
            with Session() as session:
                query = (
                    select(Workers)
                    .options(selectinload(Workers.resumes))
                )

                res = session.execute(query).unique().scalars().all()

                worker_1_resumes = res[0].resumes
                print(f"{worker_1_resumes=}")

                worker_2_resumes = res[0].resumes
                print(f"{worker_2_resumes=}")


def select_workers_with_condition_relationship():
    with Session() as session:
        query = (
            select(Workers)
            .options(selectinload(Workers.resumes_parttime))
        )

        res = session.execute(query).unique().scalars().all()

        print(f"{res=}")

def select_workers_with_contains_eager():
    with Session() as session:
        query = (
            select(Workers)
            .join(Workers.resumes)
            .options(contains_eager(Workers.resumes))
            .filter(Resumes.workload == 'parttime')
        )

        res = session.execute(query).unique().scalars().all()

        print(f"{res=}")