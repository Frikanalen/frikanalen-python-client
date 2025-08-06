from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.patched_scheduleitem_modify_request import PatchedScheduleitemModifyRequest
from ...models.scheduleitem_modify import ScheduleitemModify
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: PatchedScheduleitemModifyRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/api/scheduleitems/{id}/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ScheduleitemModify]:
    if response.status_code == 200:
        response_200 = ScheduleitemModify.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ScheduleitemModify]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedScheduleitemModifyRequest,
) -> Response[ScheduleitemModify]:
    """Video events schedule

    list:
    Query parameters
    ----------------
    `date`: YYYY-MM-DD or 'today' (Europe/Oslo). Defaults to today.

    `days`: Number of days. Defaults to 1.

    `surrounding`: Include event before and after the window.

    `ordering`: Field to order by. Prefix '-' for desc. Defaults to 'starttime'.

    Args:
        id (int):
        body (PatchedScheduleitemModifyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScheduleitemModify]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedScheduleitemModifyRequest,
) -> Optional[ScheduleitemModify]:
    """Video events schedule

    list:
    Query parameters
    ----------------
    `date`: YYYY-MM-DD or 'today' (Europe/Oslo). Defaults to today.

    `days`: Number of days. Defaults to 1.

    `surrounding`: Include event before and after the window.

    `ordering`: Field to order by. Prefix '-' for desc. Defaults to 'starttime'.

    Args:
        id (int):
        body (PatchedScheduleitemModifyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScheduleitemModify
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedScheduleitemModifyRequest,
) -> Response[ScheduleitemModify]:
    """Video events schedule

    list:
    Query parameters
    ----------------
    `date`: YYYY-MM-DD or 'today' (Europe/Oslo). Defaults to today.

    `days`: Number of days. Defaults to 1.

    `surrounding`: Include event before and after the window.

    `ordering`: Field to order by. Prefix '-' for desc. Defaults to 'starttime'.

    Args:
        id (int):
        body (PatchedScheduleitemModifyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScheduleitemModify]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    body: PatchedScheduleitemModifyRequest,
) -> Optional[ScheduleitemModify]:
    """Video events schedule

    list:
    Query parameters
    ----------------
    `date`: YYYY-MM-DD or 'today' (Europe/Oslo). Defaults to today.

    `days`: Number of days. Defaults to 1.

    `surrounding`: Include event before and after the window.

    `ordering`: Field to order by. Prefix '-' for desc. Defaults to 'starttime'.

    Args:
        id (int):
        body (PatchedScheduleitemModifyRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScheduleitemModify
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
