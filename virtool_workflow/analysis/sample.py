from pathlib import Path

from virtool_workflow import fixture
from virtool_workflow.abc.data_providers import AbstractSampleProvider
from virtool_workflow.analysis.utils import make_read_paths
from virtool_workflow.data_model.samples import Sample


@fixture
async def sample(
        sample_provider: AbstractSampleProvider,
        work_path: Path
) -> Sample:
    """
    The sample associated with the current job.

    Returns a :class:`.Sample` object.

    """
    read_path = work_path / "reads"
    read_path.mkdir()

    sample_ = await sample_provider.get()
    await sample_provider.download_reads(read_path, sample_.paired)
    sample_.reads_path = read_path
    sample_.read_paths = make_read_paths(read_path, sample_.paired)
    return sample_