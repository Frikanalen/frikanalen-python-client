import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.video_create import VideoCreate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: VideoCreate,
    categories_name_icontains: Union[Unset, list[str]] = UNSET,
    created_time_after: Union[Unset, datetime.datetime] = UNSET,
    created_time_before: Union[Unset, datetime.datetime] = UNSET,
    creator_email: Union[Unset, str] = UNSET,
    framerate: Union[Unset, int] = UNSET,
    has_tono_records: Union[Unset, bool] = UNSET,
    is_filler: Union[Unset, bool] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_icontains: Union[Unset, str] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    organization: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = 50,
    played_count_web: Union[Unset, int] = UNSET,
    played_count_web_gt: Union[Unset, int] = UNSET,
    played_count_web_gte: Union[Unset, int] = UNSET,
    played_count_web_lt: Union[Unset, int] = UNSET,
    played_count_web_lte: Union[Unset, int] = UNSET,
    proper_import: Union[Unset, bool] = UNSET,
    publish_on_web: Union[Unset, bool] = UNSET,
    q: Union[Unset, str] = UNSET,
    ref_url: Union[Unset, str] = UNSET,
    ref_url_icontains: Union[Unset, str] = UNSET,
    ref_url_startswith: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_categories_name_icontains: Union[Unset, list[str]] = UNSET
    if not isinstance(categories_name_icontains, Unset):
        json_categories_name_icontains = categories_name_icontains

    params["categories__name__icontains"] = json_categories_name_icontains

    json_created_time_after: Union[Unset, str] = UNSET
    if not isinstance(created_time_after, Unset):
        json_created_time_after = created_time_after.isoformat()
    params["created_time_after"] = json_created_time_after

    json_created_time_before: Union[Unset, str] = UNSET
    if not isinstance(created_time_before, Unset):
        json_created_time_before = created_time_before.isoformat()
    params["created_time_before"] = json_created_time_before

    params["creator__email"] = creator_email

    params["framerate"] = framerate

    params["has_tono_records"] = has_tono_records

    params["is_filler"] = is_filler

    params["name"] = name

    params["name__icontains"] = name_icontains

    params["ordering"] = ordering

    params["organization"] = organization

    params["page_size"] = page_size

    params["played_count_web"] = played_count_web

    params["played_count_web__gt"] = played_count_web_gt

    params["played_count_web__gte"] = played_count_web_gte

    params["played_count_web__lt"] = played_count_web_lt

    params["played_count_web__lte"] = played_count_web_lte

    params["proper_import"] = proper_import

    params["publish_on_web"] = publish_on_web

    params["q"] = q

    params["ref_url"] = ref_url

    params["ref_url__icontains"] = ref_url_icontains

    params["ref_url__startswith"] = ref_url_startswith

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/videos/",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[VideoCreate]:
    if response.status_code == 201:
        response_201 = VideoCreate.from_dict(response.json())

        return response_201
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[VideoCreate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: VideoCreate,
    categories_name_icontains: Union[Unset, list[str]] = UNSET,
    created_time_after: Union[Unset, datetime.datetime] = UNSET,
    created_time_before: Union[Unset, datetime.datetime] = UNSET,
    creator_email: Union[Unset, str] = UNSET,
    framerate: Union[Unset, int] = UNSET,
    has_tono_records: Union[Unset, bool] = UNSET,
    is_filler: Union[Unset, bool] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_icontains: Union[Unset, str] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    organization: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = 50,
    played_count_web: Union[Unset, int] = UNSET,
    played_count_web_gt: Union[Unset, int] = UNSET,
    played_count_web_gte: Union[Unset, int] = UNSET,
    played_count_web_lt: Union[Unset, int] = UNSET,
    played_count_web_lte: Union[Unset, int] = UNSET,
    proper_import: Union[Unset, bool] = UNSET,
    publish_on_web: Union[Unset, bool] = UNSET,
    q: Union[Unset, str] = UNSET,
    ref_url: Union[Unset, str] = UNSET,
    ref_url_icontains: Union[Unset, str] = UNSET,
    ref_url_startswith: Union[Unset, str] = UNSET,
) -> Response[VideoCreate]:
    """List and create videos.


        Provides a paginated and filterable list of videos.

        Use query parameters to refine results.


    Args:
        categories_name_icontains (Union[Unset, list[str]]):
        created_time_after (Union[Unset, datetime.datetime]):
        created_time_before (Union[Unset, datetime.datetime]):
        creator_email (Union[Unset, str]):
        framerate (Union[Unset, int]):
        has_tono_records (Union[Unset, bool]):
        is_filler (Union[Unset, bool]):
        name (Union[Unset, str]):
        name_icontains (Union[Unset, str]):
        ordering (Union[Unset, str]):
        organization (Union[Unset, int]):
        page_size (Union[Unset, int]):  Default: 50.
        played_count_web (Union[Unset, int]):
        played_count_web_gt (Union[Unset, int]):
        played_count_web_gte (Union[Unset, int]):
        played_count_web_lt (Union[Unset, int]):
        played_count_web_lte (Union[Unset, int]):
        proper_import (Union[Unset, bool]):
        publish_on_web (Union[Unset, bool]):
        q (Union[Unset, str]):
        ref_url (Union[Unset, str]):
        ref_url_icontains (Union[Unset, str]):
        ref_url_startswith (Union[Unset, str]):
        body (VideoCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VideoCreate]
    """

    kwargs = _get_kwargs(
        body=body,
        categories_name_icontains=categories_name_icontains,
        created_time_after=created_time_after,
        created_time_before=created_time_before,
        creator_email=creator_email,
        framerate=framerate,
        has_tono_records=has_tono_records,
        is_filler=is_filler,
        name=name,
        name_icontains=name_icontains,
        ordering=ordering,
        organization=organization,
        page_size=page_size,
        played_count_web=played_count_web,
        played_count_web_gt=played_count_web_gt,
        played_count_web_gte=played_count_web_gte,
        played_count_web_lt=played_count_web_lt,
        played_count_web_lte=played_count_web_lte,
        proper_import=proper_import,
        publish_on_web=publish_on_web,
        q=q,
        ref_url=ref_url,
        ref_url_icontains=ref_url_icontains,
        ref_url_startswith=ref_url_startswith,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: VideoCreate,
    categories_name_icontains: Union[Unset, list[str]] = UNSET,
    created_time_after: Union[Unset, datetime.datetime] = UNSET,
    created_time_before: Union[Unset, datetime.datetime] = UNSET,
    creator_email: Union[Unset, str] = UNSET,
    framerate: Union[Unset, int] = UNSET,
    has_tono_records: Union[Unset, bool] = UNSET,
    is_filler: Union[Unset, bool] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_icontains: Union[Unset, str] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    organization: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = 50,
    played_count_web: Union[Unset, int] = UNSET,
    played_count_web_gt: Union[Unset, int] = UNSET,
    played_count_web_gte: Union[Unset, int] = UNSET,
    played_count_web_lt: Union[Unset, int] = UNSET,
    played_count_web_lte: Union[Unset, int] = UNSET,
    proper_import: Union[Unset, bool] = UNSET,
    publish_on_web: Union[Unset, bool] = UNSET,
    q: Union[Unset, str] = UNSET,
    ref_url: Union[Unset, str] = UNSET,
    ref_url_icontains: Union[Unset, str] = UNSET,
    ref_url_startswith: Union[Unset, str] = UNSET,
) -> Optional[VideoCreate]:
    """List and create videos.


        Provides a paginated and filterable list of videos.

        Use query parameters to refine results.


    Args:
        categories_name_icontains (Union[Unset, list[str]]):
        created_time_after (Union[Unset, datetime.datetime]):
        created_time_before (Union[Unset, datetime.datetime]):
        creator_email (Union[Unset, str]):
        framerate (Union[Unset, int]):
        has_tono_records (Union[Unset, bool]):
        is_filler (Union[Unset, bool]):
        name (Union[Unset, str]):
        name_icontains (Union[Unset, str]):
        ordering (Union[Unset, str]):
        organization (Union[Unset, int]):
        page_size (Union[Unset, int]):  Default: 50.
        played_count_web (Union[Unset, int]):
        played_count_web_gt (Union[Unset, int]):
        played_count_web_gte (Union[Unset, int]):
        played_count_web_lt (Union[Unset, int]):
        played_count_web_lte (Union[Unset, int]):
        proper_import (Union[Unset, bool]):
        publish_on_web (Union[Unset, bool]):
        q (Union[Unset, str]):
        ref_url (Union[Unset, str]):
        ref_url_icontains (Union[Unset, str]):
        ref_url_startswith (Union[Unset, str]):
        body (VideoCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VideoCreate
    """

    return sync_detailed(
        client=client,
        body=body,
        categories_name_icontains=categories_name_icontains,
        created_time_after=created_time_after,
        created_time_before=created_time_before,
        creator_email=creator_email,
        framerate=framerate,
        has_tono_records=has_tono_records,
        is_filler=is_filler,
        name=name,
        name_icontains=name_icontains,
        ordering=ordering,
        organization=organization,
        page_size=page_size,
        played_count_web=played_count_web,
        played_count_web_gt=played_count_web_gt,
        played_count_web_gte=played_count_web_gte,
        played_count_web_lt=played_count_web_lt,
        played_count_web_lte=played_count_web_lte,
        proper_import=proper_import,
        publish_on_web=publish_on_web,
        q=q,
        ref_url=ref_url,
        ref_url_icontains=ref_url_icontains,
        ref_url_startswith=ref_url_startswith,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: VideoCreate,
    categories_name_icontains: Union[Unset, list[str]] = UNSET,
    created_time_after: Union[Unset, datetime.datetime] = UNSET,
    created_time_before: Union[Unset, datetime.datetime] = UNSET,
    creator_email: Union[Unset, str] = UNSET,
    framerate: Union[Unset, int] = UNSET,
    has_tono_records: Union[Unset, bool] = UNSET,
    is_filler: Union[Unset, bool] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_icontains: Union[Unset, str] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    organization: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = 50,
    played_count_web: Union[Unset, int] = UNSET,
    played_count_web_gt: Union[Unset, int] = UNSET,
    played_count_web_gte: Union[Unset, int] = UNSET,
    played_count_web_lt: Union[Unset, int] = UNSET,
    played_count_web_lte: Union[Unset, int] = UNSET,
    proper_import: Union[Unset, bool] = UNSET,
    publish_on_web: Union[Unset, bool] = UNSET,
    q: Union[Unset, str] = UNSET,
    ref_url: Union[Unset, str] = UNSET,
    ref_url_icontains: Union[Unset, str] = UNSET,
    ref_url_startswith: Union[Unset, str] = UNSET,
) -> Response[VideoCreate]:
    """List and create videos.


        Provides a paginated and filterable list of videos.

        Use query parameters to refine results.


    Args:
        categories_name_icontains (Union[Unset, list[str]]):
        created_time_after (Union[Unset, datetime.datetime]):
        created_time_before (Union[Unset, datetime.datetime]):
        creator_email (Union[Unset, str]):
        framerate (Union[Unset, int]):
        has_tono_records (Union[Unset, bool]):
        is_filler (Union[Unset, bool]):
        name (Union[Unset, str]):
        name_icontains (Union[Unset, str]):
        ordering (Union[Unset, str]):
        organization (Union[Unset, int]):
        page_size (Union[Unset, int]):  Default: 50.
        played_count_web (Union[Unset, int]):
        played_count_web_gt (Union[Unset, int]):
        played_count_web_gte (Union[Unset, int]):
        played_count_web_lt (Union[Unset, int]):
        played_count_web_lte (Union[Unset, int]):
        proper_import (Union[Unset, bool]):
        publish_on_web (Union[Unset, bool]):
        q (Union[Unset, str]):
        ref_url (Union[Unset, str]):
        ref_url_icontains (Union[Unset, str]):
        ref_url_startswith (Union[Unset, str]):
        body (VideoCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[VideoCreate]
    """

    kwargs = _get_kwargs(
        body=body,
        categories_name_icontains=categories_name_icontains,
        created_time_after=created_time_after,
        created_time_before=created_time_before,
        creator_email=creator_email,
        framerate=framerate,
        has_tono_records=has_tono_records,
        is_filler=is_filler,
        name=name,
        name_icontains=name_icontains,
        ordering=ordering,
        organization=organization,
        page_size=page_size,
        played_count_web=played_count_web,
        played_count_web_gt=played_count_web_gt,
        played_count_web_gte=played_count_web_gte,
        played_count_web_lt=played_count_web_lt,
        played_count_web_lte=played_count_web_lte,
        proper_import=proper_import,
        publish_on_web=publish_on_web,
        q=q,
        ref_url=ref_url,
        ref_url_icontains=ref_url_icontains,
        ref_url_startswith=ref_url_startswith,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: VideoCreate,
    categories_name_icontains: Union[Unset, list[str]] = UNSET,
    created_time_after: Union[Unset, datetime.datetime] = UNSET,
    created_time_before: Union[Unset, datetime.datetime] = UNSET,
    creator_email: Union[Unset, str] = UNSET,
    framerate: Union[Unset, int] = UNSET,
    has_tono_records: Union[Unset, bool] = UNSET,
    is_filler: Union[Unset, bool] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_icontains: Union[Unset, str] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    organization: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = 50,
    played_count_web: Union[Unset, int] = UNSET,
    played_count_web_gt: Union[Unset, int] = UNSET,
    played_count_web_gte: Union[Unset, int] = UNSET,
    played_count_web_lt: Union[Unset, int] = UNSET,
    played_count_web_lte: Union[Unset, int] = UNSET,
    proper_import: Union[Unset, bool] = UNSET,
    publish_on_web: Union[Unset, bool] = UNSET,
    q: Union[Unset, str] = UNSET,
    ref_url: Union[Unset, str] = UNSET,
    ref_url_icontains: Union[Unset, str] = UNSET,
    ref_url_startswith: Union[Unset, str] = UNSET,
) -> Optional[VideoCreate]:
    """List and create videos.


        Provides a paginated and filterable list of videos.

        Use query parameters to refine results.


    Args:
        categories_name_icontains (Union[Unset, list[str]]):
        created_time_after (Union[Unset, datetime.datetime]):
        created_time_before (Union[Unset, datetime.datetime]):
        creator_email (Union[Unset, str]):
        framerate (Union[Unset, int]):
        has_tono_records (Union[Unset, bool]):
        is_filler (Union[Unset, bool]):
        name (Union[Unset, str]):
        name_icontains (Union[Unset, str]):
        ordering (Union[Unset, str]):
        organization (Union[Unset, int]):
        page_size (Union[Unset, int]):  Default: 50.
        played_count_web (Union[Unset, int]):
        played_count_web_gt (Union[Unset, int]):
        played_count_web_gte (Union[Unset, int]):
        played_count_web_lt (Union[Unset, int]):
        played_count_web_lte (Union[Unset, int]):
        proper_import (Union[Unset, bool]):
        publish_on_web (Union[Unset, bool]):
        q (Union[Unset, str]):
        ref_url (Union[Unset, str]):
        ref_url_icontains (Union[Unset, str]):
        ref_url_startswith (Union[Unset, str]):
        body (VideoCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        VideoCreate
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            categories_name_icontains=categories_name_icontains,
            created_time_after=created_time_after,
            created_time_before=created_time_before,
            creator_email=creator_email,
            framerate=framerate,
            has_tono_records=has_tono_records,
            is_filler=is_filler,
            name=name,
            name_icontains=name_icontains,
            ordering=ordering,
            organization=organization,
            page_size=page_size,
            played_count_web=played_count_web,
            played_count_web_gt=played_count_web_gt,
            played_count_web_gte=played_count_web_gte,
            played_count_web_lt=played_count_web_lt,
            played_count_web_lte=played_count_web_lte,
            proper_import=proper_import,
            publish_on_web=publish_on_web,
            q=q,
            ref_url=ref_url,
            ref_url_icontains=ref_url_icontains,
            ref_url_startswith=ref_url_startswith,
        )
    ).parsed
